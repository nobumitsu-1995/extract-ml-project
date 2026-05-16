from CONST import LABEL_LIST
import json
import torch
from transformers import BertTokenizerFast, BertForTokenClassification

MODEL_DIR = "./trained_model"

_model = None
_tokenizer = None
_device = None


def _load():
    global _model, _tokenizer, _device
    if _model is None:
        _tokenizer = BertTokenizerFast.from_pretrained(MODEL_DIR)
        _model = BertForTokenClassification.from_pretrained(MODEL_DIR)
        _device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        _model.to(_device)
        _model.eval()
    return _model, _tokenizer, _device


def extract_to_json(text):
    model, tokenizer, device = _load()

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=2).squeeze().tolist()
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())

    result_json = {}
    current_entity = None
    current_label = None

    for token, pred_id in zip(tokens, predictions):
        if token in ["[CLS]", "[SEP]", "[PAD]"]:
            continue

        label = LABEL_LIST[pred_id]
        # ## を除去（サブワードの結合）
        clean_token = token.replace('##', '')

        if label.startswith("B-"):
            new_label = label.split("-")[1]
            # 同じラベルの B- が連続する場合は結合（途中で誤って B- に切り替わるケース対策）
            if current_label == new_label and current_entity is not None:
                current_entity += clean_token
            else:
                # 別ラベルへの遷移時は直前のエンティティを保存
                if current_entity and current_label not in result_json:
                    result_json[current_label] = current_entity
                current_label = new_label
                current_entity = clean_token
        elif label.startswith("I-") and current_label == label.split("-")[1]:
            # エンティティの継続
            if current_entity is not None:
                current_entity += clean_token
        else:
            # エンティティの終了
            if current_entity:
                # 既に同じラベルがあればリストにするか、最初に見つけたものを優先
                if current_label not in result_json:
                    result_json[current_label] = current_entity
                current_entity = None
                current_label = None

    # 最後のエンティティを処理
    if current_entity and current_label not in result_json:
        result_json[current_label] = current_entity

    return result_json


if __name__ == "__main__":
    test_text = "Ruby開発案件。現場は渋谷。単価は70万。"
    extracted_data = extract_to_json(test_text)

    print(f"\n--- 最終的なJSON出力 ---")
    print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
