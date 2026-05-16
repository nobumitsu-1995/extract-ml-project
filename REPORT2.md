# ベースモデル比較実験

`REPORT.md` の実験8 で 100% を達成した構成（`extract.py` の align+原文スライス、`main.py` の手動 offset 学習）はそのままに、**ベースモデルだけを差し替え**て精度・学習挙動を比較する。

## 評価条件（共通）

- TRAIN_DATA: 91件、TEST_DATA: 28件（実験8 と同じ。`｜` や `React Native` も原文のまま）
- epoch: 20
- バッチサイズ: 2
- 学習率: 5e-5
- 最大トークン長: 128
- デバイス: MPS (Apple Silicon)
- tokenizer: モデルに応じて `BertJapaneseTokenizer` / Fast tokenizer / `DistilBertJapaneseTokenizer` / `MLukeTokenizer`
- 評価指標: 完全一致率（TITLE/SUMMARY/PRICE すべて正解）と各ラベル別正解率

差し替えるのは `main.py` の `MODEL_NAME` のみ。学習・推論コードは AutoTokenizer/AutoModelForTokenClassification + `is_fast` 分岐で汎用化済み。Fast tokenizer は `return_offsets_mapping=True`、Slow tokenizer は手書きの `align_token_offsets` を使う。

## 比較対象モデル

| ID | モデル名 | 特徴 |
| --- | --- | --- |
| baseline | `cl-tohoku/bert-base-japanese-v3` | 現状ベース（実験8）。base サイズ。WordPiece (MeCab pre-tokenize) |
| M1 | `cl-tohoku/bert-base-japanese-v2` | v3 の前世代 |
| M2 | `cl-tohoku/bert-base-japanese-char-v3` | 文字レベル分割（subword なし） |
| M3 | `cl-tohoku/bert-large-japanese-v2` | large サイズ（パラメータ約3倍） |
| M4 | `ku-nlp/deberta-v2-base-japanese` | 京大 DeBERTa-v2、SentencePiece、Fast tokenizer 対応 |
| M5 | `rinna/japanese-roberta-base` | rinna 製 RoBERTa、T5Tokenizer (SentencePiece) ベース |
| M6 | `xlm-roberta-base` | 多言語 RoBERTa、100言語事前学習 |
| M7 | `line-corporation/line-distilbert-base-japanese` | LINE 製 DistilBERT、軽量モデル |
| M8 | `studio-ousia/luke-japanese-base-lite` | LUKE Japanese、エンティティ認識指向の事前学習 |

## 実験記録

### Baseline: bert-base-japanese-v3 (REPORT.md 実験8 と同条件)

| 指標 | 値 |
| --- | --- |
| 最終 Loss | 0.0005 |
| 完全一致 | **28/28 (100.0%)** |
| TITLE | 28/28 (100.0%) |
| SUMMARY | 28/28 (100.0%) |
| PRICE | 28/28 (100.0%) |

### M1: cl-tohoku/bert-base-japanese-v2

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0039 | ↑（後半に Loss 発散：epoch 11=0.0545, 13=0.0617） |
| 完全一致 | **25/28 (89.3%)** | -3 (-10.7pt) |
| TITLE | 25/28 (89.3%) | -3 |
| SUMMARY | 27/28 (96.4%) | -1 |
| PRICE | 28/28 (100.0%) | ±0 |

**失敗ケース**

| # | 失敗ラベル | 予測 | 正解 |
| --- | --- | --- | --- |
| 12 | TITLE / SUMMARY | `Dev` / `CI` | `DevOps` / `CI/CDパイプライン構築` |
| 18 | TITLE | `金融` | `金融系プロジェクト` |
| 24 | TITLE | `Java` | `Java案件` |

**所見**: TITLE のスパンが早く切れる傾向。v2 は v3 より sub-word 分割の粒度が違うのか、または epoch 後半の Loss 発散の影響と推測。

### M2: cl-tohoku/bert-base-japanese-char-v3

文字レベル分割（subword なし）。1 文字 = 1 token。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0174 | ↑（後半で発散） |
| 完全一致 | **26/28 (92.9%)** | -2 (-7.1pt) |
| TITLE | 28/28 (100.0%) | ±0 |
| SUMMARY | 26/28 (92.9%) | -2 |
| PRICE | 28/28 (100.0%) | ±0 |

**失敗ケース**

| # | 失敗ラベル | 予測 | 正解 |
| --- | --- | --- | --- |
| 15 | SUMMARY | `Se` | `Seleniumでの自動化推進` |
| 26 | SUMMARY | `An` | `Androidアプリの新機能追加` |

**所見**

- TITLE は100%。日本語＋短い英単語混じりの TITLE には強い。
- 一方、SUMMARY 内に **長めの英単語（Selenium / Android）が現れる**と、最初の2〜3文字でラベルが途切れる。文字レベル分割では英字も1文字ずつ tokenize されるため、長い英単語の中で I- ラベル予測が不安定になりやすい。
- 文字レベルは未知語に強い一方、英字連続箇所では subword 系の方が有利と分かる。

### M3: cl-tohoku/bert-large-japanese-v2

base の約3倍のパラメータ規模。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0344 | ↑（学習が不安定。epoch 14=0.2653, 15=0.1431 で再発散） |
| 完全一致 | **26/28 (92.9%)** | -2 (-7.1pt) |
| TITLE | 28/28 (100.0%) | ±0 |
| SUMMARY | 26/28 (92.9%) | -2 |
| PRICE | 28/28 (100.0%) | ±0 |

**失敗ケース**

| # | 失敗ラベル | 予測 | 正解 |
| --- | --- | --- | --- |
| 4 | SUMMARY | `学習モデルのチューニング` | `機械学習モデルのチューニング` |
| 18 | SUMMARY | ``（空） | `システム再構築の支援` |

**所見**

- large 化で精度が上がるわけではなく、むしろ baseline (v3 base) より低い。
- 学習データ91件に対してパラメータ規模が大きすぎ、20 epoch では収束しきれていない印象。epoch 後半に Loss が再上昇している。
- TITLE は安定して100%だが、SUMMARY は #4 で先頭の「機械」が欠落、#18 では完全に空抜けと、頭・全体が落ちるタイプの誤り。
- 学習データ量に対して過剰なモデルサイズは、epoch 数・学習率の再調整なしには baseline を超えられない。

### M4: ku-nlp/deberta-v2-base-japanese

京大製 DeBERTa-v2、SentencePiece の Fast tokenizer。

**初回試行（offset 補正前）**: 22/28 (78.6%)。SUMMARY が空抜けする失敗が多発（#3, #6, #14, #16, #17, #20）。原因は SentencePiece 系 Fast tokenizer の `offset_mapping` が「トークンが含む先頭の空白の位置」を返すため、`char_labels[start]` が `O` を引いてしまい B-/I- ラベルが付与されない問題。

`extract.py:get_aligned_offsets` で**先頭空白を `start` から読み飛ばす補正**を入れて再学習。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0079 | ↑ |
| 完全一致 | **27/28 (96.4%)** | -1 (-3.6pt) |
| TITLE | 28/28 (100.0%) | ±0 |
| SUMMARY | 27/28 (96.4%) | -1 |
| PRICE | 28/28 (100.0%) | ±0 |

**失敗ケース**

| # | 失敗ラベル | 予測 | 正解 |
| --- | --- | --- | --- |
| 2 | SUMMARY | `：管理画面のリプレース` | `管理画面のリプレース` |

**所見**

- 「概要：管理画面…」の `：` を SUMMARY の先頭に含めてしまう軽微な誤り。train データの粒度を揃えれば解決可能と推測。
- SentencePiece 系を使う際は offset 取得時の**先頭空白スキップ**が必須。これは Fast tokenizer 全般で必要になる重要な実装ポイント。
- baseline には届かないが、SentencePiece＋Fast tokenizer 系の中では最も安定。

### M5: rinna/japanese-roberta-base

rinna 製 RoBERTa、T5Tokenizer ベース（SentencePiece）。`tiktoken`/`sentencepiece` を追加インストール後、`T5TokenizerFast` として動作。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.1203 | ↑↑（収束しきれていない） |
| 完全一致 | **0/28 (0.0%)** | -28 (-100pt) |
| TITLE | 26/28 (92.9%) | -2 |
| SUMMARY | 27/28 (96.4%) | -1 |
| PRICE | 0/28 (0.0%) | -28 |

**所見**

- **PRICE が完全に 0%**。`70万`・`85万円`・`MAX110万` など全件で抽出に失敗。Loss も 20 epoch で 0.12 までしか下がらず学習が大幅に不足。
- このモデルは（公式 README 上）入力に `[CLS]` を手動で先頭付与することが推奨されているが、AutoTokenizer 経由では自動付与されないため、位置埋め込みのズレ等で学習が安定しなかった可能性が高い。
- さらに英字（`R`, `S` 等の単独 Latin 文字）が SentencePiece の語彙に無く `<unk>` 化される問題もあり、token 単位の対応付けが脆い。
- 採用するなら CLS 手動挿入＋語彙拡張等、追加対応が前提。**そのまま差し替えは不可**という結論。

### M6: xlm-roberta-base

多言語 RoBERTa、100言語事前学習、SentencePiece Fast tokenizer。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0127 | ↑（中盤で発散するが 20 epoch 内に再収束） |
| 完全一致 | **28/28 (100.0%)** | ±0 |
| TITLE | 28/28 (100.0%) | ±0 |
| SUMMARY | 28/28 (100.0%) | ±0 |
| PRICE | 28/28 (100.0%) | ±0 |

**所見**

- baseline と並ぶ **100% 達成**。日本語特化モデルでなくても、十分な多言語事前学習があれば本タスクには対応可能と判明。
- Loss は baseline (v3 = 0.0005) より一桁高いが、テスト誤りはゼロ。
- パラメータ数は base 相当だが多言語ゆえ語彙が大きく（25万）、モデルサイズは v3 より大きい。学習・推論ともにやや重い。
- 日本語特化を選ぶ理由が薄まる結果。**「日本語以外も扱うかもしれない」用途では XLM-R が有力候補**。

### M7: line-corporation/line-distilbert-base-japanese

LINE 製 DistilBERT、独自 `DistilBertJapaneseTokenizer`（SentencePiece スタイル + Latin 小文字化、slow）。`trust_remote_code=True` が必要。

`align_token_offsets` を **▁ プレフィックスの SP 形式**にも対応させた（BertJapaneseTokenizer の `##` 形式とは subword 規約が逆なので、トークン列全体を見て自動判別）。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0003 | ↓（最も収束が綺麗） |
| 完全一致 | **28/28 (100.0%)** | ±0 |
| TITLE | 28/28 (100.0%) | ±0 |
| SUMMARY | 28/28 (100.0%) | ±0 |
| PRICE | 28/28 (100.0%) | ±0 |

**所見**

- baseline と同じ **100% 達成**、しかも最終 Loss は本実験中最良の 0.0003。
- DistilBERT 系で base モデルの 6 層化（パラメータ数約半分）にも関わらず、本タスクには十分。
- 推論速度・モデルサイズの面で有利。**性能を落とさず軽量化したい場合の第一候補**。

### M8: studio-ousia/luke-japanese-base-lite

LUKE Japanese（エンティティ認識指向の事前学習）、`MLukeTokenizer`（slow、SentencePiece ベース）。

| 指標 | 値 | baseline 比 |
| --- | --- | --- |
| 最終 Loss | 0.0309 | ↑（後半 epoch 13=0.1459 で再発散） |
| 完全一致 | **24/28 (85.7%)** | -4 (-14.3pt) |
| TITLE | 26/28 (92.9%) | -2 |
| SUMMARY | 25/28 (89.3%) | -3 |
| PRICE | 28/28 (100.0%) | ±0 |

**失敗ケース**

| # | 失敗ラベル | 予測 | 正解 |
| --- | --- | --- | --- |
| 7 | SUMMARY | `インフラ設計から運用` | `インフラ設計から運用まで` |
| 12 | TITLE / SUMMARY | `DevO` / `C` | `DevOps` / `CI/CDパイプライン構築` |
| 15 | SUMMARY | `Se` | `Seleniumでの自動化推進` |
| 18 | TITLE | `金融系` | `金融系プロジェクト` |

**所見**

- 「エンティティ認識特化」を謳う事前学習にも関わらず、本タスクでは baseline 比 -14.3pt と振るわず。
- 失敗パターンは M2 (char-v3) に似て、**英単語の途中で I- 予測が途切れる**ケースが顕著（`DevO`, `C`, `Se`）。
- `LukeForTokenClassification` を `entity_ids` なしで動かしているため、本来 LUKE の強みであるエンティティ表現を活かせていない可能性が高い。LUKE 本来の能力を引き出すには、入力に注釈付きエンティティスパンを与える特殊な前処理が必要で、本タスクとは噛み合わない。
- LUKE は **質問応答・関係抽出など、明示的なエンティティ入力がある下流タスク向け**であり、生の NER をゼロから学習させる用途には不向きと判断。

## 比較まとめ

| ID | モデル | 完全一致 | TITLE | SUMMARY | PRICE | 最終 Loss |
| --- | --- | --- | --- | --- | --- | --- |
| baseline | bert-base-japanese-v3 | **28/28 (100.0%)** | 100.0% | 100.0% | 100.0% | 0.0005 |
| M1 | bert-base-japanese-v2 | 25/28 (89.3%) | 89.3% | 96.4% | 100.0% | 0.0039 |
| M2 | bert-base-japanese-char-v3 | 26/28 (92.9%) | 100.0% | 92.9% | 100.0% | 0.0174 |
| M3 | bert-large-japanese-v2 | 26/28 (92.9%) | 100.0% | 92.9% | 100.0% | 0.0344 |
| M4 | deberta-v2-base-japanese | 27/28 (96.4%) | 100.0% | 96.4% | 100.0% | 0.0079 |
| M5 | rinna/japanese-roberta-base | 0/28 (0.0%) | 92.9% | 96.4% | 0.0% | 0.1203 |
| M6 | xlm-roberta-base | **28/28 (100.0%)** | 100.0% | 100.0% | 100.0% | 0.0127 |
| M7 | line-distilbert-base-japanese | **28/28 (100.0%)** | 100.0% | 100.0% | 100.0% | **0.0003** |
| M8 | luke-japanese-base-lite | 24/28 (85.7%) | 92.9% | 89.3% | 100.0% | 0.0309 |

### 結論

#### 性能順序（本タスクでの完全一致率）

1. **同率1位 (100%)**: baseline (v3) / M6 (XLM-R) / M7 (LINE DistilBERT)
2. **96.4%**: M4 (DeBERTa-v2)
3. **92.9%**: M2 (char-v3) / M3 (large)
4. **89.3%**: M1 (v2)
5. **85.7%**: M8 (LUKE)
6. **0%**: M5 (rinna)

#### 各群別の所見

1. **cl-tohoku 系（baseline, M1, M2, M3）**: v3 base が最良。v2 → v3 の世代更新は効果あり。char-v3 は TITLE で100%だが英字長語の SUMMARY で弱い。large は本データ量では効果なし。
2. **SentencePiece + Fast tokenizer 系（M4, M6）**: ともに高精度。ただし**先頭空白を `start` から読み飛ばす offset 補正が必須**。これを入れない初期実装では M4 が 78.6% に留まった。
3. **特殊・尖ったモデル（M5, M8）**:
   - **M5 (rinna)**: そのままでは使い物にならず（CLS 自動付与なし／Latin 文字 `<unk>` 化）。AutoTokenizer 経由ではモデル設計の前提が満たされないケースがあると判明。
   - **M8 (LUKE)**: エンティティ認識向けの事前学習だが、`entity_ids` を渡さない素朴な token classification では強みを活かせない。
4. **軽量モデル（M7）**: LINE DistilBERT は **base 並みの精度 (100%)** を最小コストで達成。Loss 収束も最良の 0.0003。**速度／メモリ重視の本番投入には第一候補**。
5. **多言語モデル（M6）**: XLM-R は日本語特化でないにも関わらず 100% 到達。多言語コーパスを扱う前提が少しでもあるなら有力。

#### 実装面で得た知見

- **Fast tokenizer の `offset_mapping` は SentencePiece 系で先頭空白を含む**ことがある。NER の char-level label 付与時は、空白を `start` から advance する補正を必ず入れる。
- **slow tokenizer のサブワード規約はモデル系統ごとに逆**。BertJapaneseTokenizer は「ヘッドが prefix なし、subword に `##`」、SentencePiece slow は「ヘッドに `▁`、subword は prefix なし」。トークン列全体を見て自動判別する実装が安全。
- **`trust_remote_code=True` が必要なモデル**（LINE DistilBERT 等）は AutoTokenizer/AutoModel 共に明示指定が必要。

#### 総合判断

- 「精度最優先・本番用途」**baseline (v3)** または **M7 (LINE DistilBERT)** ← Loss 収束が綺麗な分、M7 が若干安心。サイズも小さく推論コスト最良。
- 「多言語対応必須」**M6 (XLM-R)**。
- 「日本語特化＋最新世代」**M4 (DeBERTa-v2)** も僅差で射程内、追加実験で baseline 超えの余地あり。
- **rinna (M5) と LUKE (M8) は本タスクには不向き**。
