from CONST import LABEL_MAP, TRAIN_DATA, LABEL_LIST
import torch
from torch.utils.data import DataLoader, Dataset
from torch.optim import AdamW
from transformers import BertTokenizerFast, BertForTokenClassification

MODEL_NAME = "cl-tohoku/bert-base-japanese-v3"
MODEL_DIR = "./trained_model"

# 1. 実践的なDatasetクラス
class SESExtractionDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=128):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        text = item["text"]

        # 1文字ごとのラベル配列を初期化
        char_labels = ["O"] * len(text)
        for sub_text, label in item["labels"]:
            start = text.find(sub_text)
            if start != -1:
                char_labels[start] = f"B-{label}"
                for i in range(start + 1, start + len(sub_text)):
                    char_labels[i] = f"I-{label}"

        # トークナイズ（offset_mappingで文字とトークンを紐付け）
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_offsets_mapping=True,
            return_tensors="pt"
        )

        labels = []
        offsets = encoding['offset_mapping'].squeeze().tolist()

        for start, end in offsets:
            if start == end:  # [CLS], [SEP], [PAD] など
                labels.append(-100)
            else:
                # トークンの開始位置の文字ラベルを採用
                labels.append(LABEL_MAP.get(char_labels[start], 0))

        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(labels)
        }


# 2. 学習
def train():
    tokenizer = BertTokenizerFast.from_pretrained(MODEL_NAME)
    model = BertForTokenClassification.from_pretrained(MODEL_NAME, num_labels=len(LABEL_LIST))

    # Macならmps, Windowsならcuda
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model.to(device)

    dataset = SESExtractionDataset(TRAIN_DATA, tokenizer)
    loader = DataLoader(dataset, batch_size=2, shuffle=True)
    optimizer = AdamW(model.parameters(), lr=5e-5)

    model.train()
    print("Training started...")
    for epoch in range(20):
        total_loss = 0
        for batch in loader:
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/20 - Loss: {total_loss/len(loader):.4f}")

    model.save_pretrained(MODEL_DIR)
    tokenizer.save_pretrained(MODEL_DIR)
    print(f"Model saved to {MODEL_DIR}")


if __name__ == "__main__":
    train()
