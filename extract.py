from CONST import LABEL_LIST
import json
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_DIR = "./trained_model"

_model = None
_tokenizer = None
_device = None


def _load():
    global _model, _tokenizer, _device
    if _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, trust_remote_code=True)
        _model = AutoModelForTokenClassification.from_pretrained(MODEL_DIR, trust_remote_code=True)
        _device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        _model.to(_device)
        _model.eval()
    return _model, _tokenizer, _device


def _special_ids(tokenizer):
    ids = {getattr(tokenizer, n, None) for n in
           ['cls_token_id', 'sep_token_id', 'pad_token_id', 'bos_token_id', 'eos_token_id']}
    ids.discard(None)
    return ids


def align_token_offsets(text, tokens):
    """Slow tokenizer 用に手動で (start,end) を求める。"""
    offsets = []
    pos = 0
    sp_style = any(t.startswith("\u2581") for t in tokens)
    for token in tokens:
        if token in ("[UNK]", "<unk>"):
            while pos < len(text) and text[pos].isspace():
                pos += 1
            if pos < len(text):
                offsets.append((pos, pos + 1))
                pos += 1
            else:
                offsets.append(None)
            continue

        if sp_style:
            if token.startswith("\u2581"):
                is_subword = False
                clean = token[1:]
            else:
                is_subword = True
                clean = token
        else:
            if token.startswith("##"):
                is_subword = True
                clean = token[2:]
            else:
                is_subword = False
                clean = token
        if not clean:
            offsets.append(None)
            continue

        if not is_subword:
            while pos < len(text) and text[pos].isspace():
                pos += 1

        if text[pos:pos + len(clean)].lower() == clean.lower():
            offsets.append((pos, pos + len(clean)))
            pos += len(clean)
        else:
            idx = text.lower().find(clean.lower(), pos)
            if idx == -1:
                offsets.append(None)
            else:
                offsets.append((idx, idx + len(clean)))
                pos = idx + len(clean)
    return offsets


def get_aligned_offsets(text, tokenizer, encoding):
    """input_ids と 1:1 で並ぶ (input_id, Optional[(start,end)]) のリスト。"""
    input_ids = encoding['input_ids'].squeeze().tolist()
    specials = _special_ids(tokenizer)
    if tokenizer.is_fast and 'offset_mapping' in encoding:
        raw = encoding['offset_mapping'].squeeze().tolist()
        result = []
        for tid, off in zip(input_ids, raw):
            s, e = int(off[0]), int(off[1])
            if tid in specials or s == e:
                result.append((tid, None))
                continue
            while s < e and s < len(text) and text[s].isspace():
                s += 1
            if s == e:
                result.append((tid, None))
            else:
                result.append((tid, (s, e)))
        return result
    raw_tokens = tokenizer.tokenize(text)
    raw_offsets = align_token_offsets(text, raw_tokens)
    result = []
    token_idx = 0
    for tid in input_ids:
        if tid in specials:
            result.append((tid, None))
            continue
        if token_idx >= len(raw_offsets):
            result.append((tid, None))
            continue
        result.append((tid, raw_offsets[token_idx]))
        token_idx += 1
    return result


def extract_to_json(text):
    model, tokenizer, device = _load()

    tok_kwargs = dict(return_tensors="pt", truncation=True, padding=True)
    if tokenizer.is_fast:
        tok_kwargs["return_offsets_mapping"] = True
    encoding = tokenizer(text, **tok_kwargs)

    model_inputs = {k: v.to(device) for k, v in encoding.items() if k != 'offset_mapping'}
    with torch.no_grad():
        outputs = model(**model_inputs)

    predictions = torch.argmax(outputs.logits, dim=2).squeeze().tolist()
    aligned = get_aligned_offsets(text, tokenizer, encoding)

    result_json = {}
    current_label = None
    current_start = None
    current_end = None

    def flush():
        nonlocal current_label, current_start, current_end
        if current_label and current_start is not None and current_label not in result_json:
            result_json[current_label] = text[current_start:current_end]
        current_label = None
        current_start = None
        current_end = None

    for (tid, off), pred_id in zip(aligned, predictions):
        if off is None:
            flush()
            continue
        start, end = off
        label = LABEL_LIST[pred_id]

        if label.startswith("B-"):
            new_label = label[2:]
            if current_label == new_label and current_start is not None:
                current_end = end
            else:
                flush()
                current_label = new_label
                current_start = start
                current_end = end
        elif label.startswith("I-") and current_label == label[2:]:
            current_end = end
        else:
            flush()

    flush()
    return result_json


if __name__ == "__main__":
    test_text = "Ruby開発案件。現場は渋谷。単価は70万。"
    extracted_data = extract_to_json(test_text)

    print(f"\n--- 最終的なJSON出力 ---")
    print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
