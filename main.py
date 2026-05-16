from CONST import LABEL_MAP, TRAIN_DATA, LABEL_LIST
from extract import align_token_offsets
import torch
from torch.utils.data import DataLoader, Dataset
from torch.optim import AdamW
from transformers import BertJapaneseTokenizer, BertForTokenClassification

MODEL_NAME = "cl-tohoku/bert-base-japanese-v3"
MODEL_DIR = "./trained_model"


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

        char_labels = ["O"] * len(text)
        for sub_text, label in item["labels"]:
            start = text.find(sub_text)
            if start != -1:
                char_labels[start] = f"B-{label}"
                for i in range(start + 1, start + len(sub_text)):
                    char_labels[i] = f"I-{label}"

        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors="pt"
        )
        input_ids = encoding['input_ids'].squeeze().tolist()

        raw_tokens = self.tokenizer.tokenize(text)
        offsets = align_token_offsets(text, raw_tokens)

        special_ids = {self.tokenizer.cls_token_id, self.tokenizer.sep_token_id, self.tokenizer.pad_token_id}

        labels = []
        token_idx = 0
        for tid in input_ids:
            if tid in special_ids:
                labels.append(-100)
                continue
            if token_idx >= len(offsets) or offsets[token_idx] is None:
                labels.append(0)
                token_idx += 1
                continue
            start, _ = offsets[token_idx]
            token_idx += 1
            if start < len(char_labels):
                labels.append(LABEL_MAP.get(char_labels[start], 0))
            else:
                labels.append(0)

        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(labels)
        }


def train():
    tokenizer = BertJapaneseTokenizer.from_pretrained(MODEL_NAME)
    model = BertForTokenClassification.from_pretrained(MODEL_NAME, num_labels=len(LABEL_LIST))

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
