# extract-ml-project

日本語の 案件メールから **タイトル（TITLE）**・**概要（SUMMARY）**・**単価（PRICE）** を抽出する固有表現抽出（NER）プロジェクトです。

東北大版 BERT (`cl-tohoku/bert-base-japanese-v3`) をファインチューニングし、BIO 形式（`O`, `B-TITLE`, `I-TITLE`, `B-SUMMARY`, `I-SUMMARY`, `B-PRICE`, `I-PRICE`）でトークン分類を行います。

## ファイル構成

| ファイル           | 役割                                                                      |
| ------------------ | ------------------------------------------------------------------------- |
| `CONST.py`         | 学習用データ `TRAIN_DATA` とテスト用データ `TEST_DATA`、ラベル定義        |
| `main.py`          | BERT ファインチューニング（学習）スクリプト                               |
| `predict.py`       | 学習済みモデルを使い、トークン単位の予測ラベルを表示                      |
| `extract.py`       | 学習済みモデルを使い、抽出結果を JSON 形式で返す `extract_to_json()` 関数 |
| `test.py`          | `TEST_DATA` を使った精度評価スクリプト                                    |
| `requirements.txt` | 依存パッケージ                                                            |
| `trained_model/`   | 学習後に生成される学習済みモデル（gitignore 対象）                        |

## セットアップ

Python 3.10 以上を推奨します（macOS の場合は MPS 対応のため `torch>=2.0` が必要）。

```bash
# 1. リポジトリのクローン
git clone <repository-url>
cd extract-ml-project

# 2. 仮想環境の作成・有効化
python3 -m venv .venv
source .venv/bin/activate

# 3. 依存パッケージのインストール
pip install -r requirements.txt
```

学習・推論時に Hugging Face Hub から `cl-tohoku/bert-base-japanese-v3` を自動ダウンロードします。初回はネットワーク接続が必要です。

> macOS の Apple Silicon では MPS、それ以外では CPU で動作します。CUDA を使いたい場合は `main.py` / `predict.py` / `extract.py` 内の `device` 判定を書き換えてください。

## 使い方

### 1. 学習データの編集（任意）

`CONST.py` の `TRAIN_DATA` に学習サンプルを追加します。各サンプルは `text`（生文）と `labels`（抽出対象のスパンとラベルのタプルリスト）から構成されます。`labels` で指定されなかった文字は自動的に `O`（無関係）になります。

```python
{
    "text": "Python開発案件。現場は赤坂。単価75万。",
    "labels": [
        ("Python開発案件", "TITLE"),
        ("現場は赤坂", "SUMMARY"),
        ("75万", "PRICE"),
    ],
}
```

### 2. モデルの学習

```bash
python main.py
```

10 エポック学習後、`./trained_model/` にモデルとトークナイザが保存されます。

### 3. 推論（トークン単位の表示）

```bash
python predict.py
```

`predict.py` 末尾の `predict("Ruby開発案件。現場は渋谷。単価は70万。")` を編集すると任意のテキストで試せます。

### 4. JSON 形式での抽出

```bash
python extract.py
```

出力例:

```json
{
  "TITLE": "Ruby開発案件",
  "SUMMARY": "現場は渋谷",
  "PRICE": "70万"
}
```

他スクリプトから関数として呼び出すこともできます。

```python
from extract import extract_to_json

result = extract_to_json("Java開発案件。基幹業務システム改修。単価80万。")
print(result)
```

### 5. 精度評価

`CONST.py` の `TEST_DATA` を用いて、完全一致率とラベル別の正解率を計測します。

```bash
python test.py
```
