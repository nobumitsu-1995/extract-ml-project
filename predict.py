from CONST import LABEL_LIST
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_DIR = "./trained_model"


def predict(text):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, trust_remote_code=True)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_DIR, trust_remote_code=True)
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model.to(device)
    model.eval()

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=2).squeeze().tolist()
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())

    special = set(tokenizer.all_special_tokens)
    print(f"\n--- 抽出結果: {text} ---")
    for token, pred_id in zip(tokens, predictions):
        if token in special:
            continue
        label = LABEL_LIST[pred_id]
        if label != "O":
            print(f"{token.replace('##', ''):10} : {label}")


if __name__ == "__main__":
    predict("【急募】Swift開発 iOSアプリの新機能追加 単価80万円")
    predict("Django開発 BtoC向けWebサービス構築 単価80万円")
    predict("Vue.js開発案件 SPAの実装担当 費用65万")
