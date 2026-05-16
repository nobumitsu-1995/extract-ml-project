from CONST import LABEL_LIST
import json
import torch
from transformers import BertJapaneseTokenizer, BertForTokenClassification

MODEL_DIR = "./trained_model"

_model = None
_tokenizer = None
_device = None


def _load():
    global _model, _tokenizer, _device
    if _model is None:
        _tokenizer = BertJapaneseTokenizer.from_pretrained(MODEL_DIR)
        _model = BertForTokenClassification.from_pretrained(MODEL_DIR)
        _device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        _model.to(_device)
        _model.eval()
    return _model, _tokenizer, _device


def align_token_offsets(text, tokens):
    """
    Slow tokenizer は offset_mapping を返さないので、トークン列を原文と
    手動でアラインして各トークンの (start, end) 文字位置を返す。
    ##接頭辞は直前トークンの直後に続くものとして扱い、非##トークンの前は
    空白読み飛ばし可とする。[UNK] は次の非空白1文字に対応とみなす。
    アライン失敗時は None を返す。
    """
    offsets = []
    pos = 0
    for token in tokens:
        if token == "[UNK]":
            while pos < len(text) and text[pos].isspace():
                pos += 1
            if pos < len(text):
                offsets.append((pos, pos + 1))
                pos += 1
            else:
                offsets.append(None)
            continue

        is_subword = token.startswith("##")
        clean = token[2:] if is_subword else token
        if not clean:
            offsets.append(None)
            continue

        if not is_subword:
            while pos < len(text) and text[pos].isspace():
                pos += 1

        if text[pos:pos + len(clean)] == clean:
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


def extract_to_json(text):
    model, tokenizer, device = _load()

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=2).squeeze().tolist()
    input_ids = inputs["input_ids"].squeeze().tolist()

    raw_tokens = tokenizer.tokenize(text)
    offsets = align_token_offsets(text, raw_tokens)

    special_ids = {tokenizer.cls_token_id, tokenizer.sep_token_id, tokenizer.pad_token_id}

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

    token_idx = 0
    for tid, pred_id in zip(input_ids, predictions):
        if tid in special_ids:
            flush()
            continue
        if token_idx >= len(offsets):
            break

        offset = offsets[token_idx]
        token_idx += 1
        label = LABEL_LIST[pred_id]

        if offset is None:
            continue
        start, end = offset

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
