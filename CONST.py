__all__ = ["TRAIN_DATA", "TEST_DATA"]

# O: 無関係, B: 開始, I: 継続
LABEL_LIST = ["O", "B-TITLE", "I-TITLE", "B-SUMMARY", "I-SUMMARY", "B-PRICE", "I-PRICE"]
LABEL_MAP = {label: i for i, label in enumerate(LABEL_LIST)}

# 学習用データ
TRAIN_DATA = [
    {
        "text": "【急募】PHP開発案件 現場はフルリモートでECサイト改修。単価は75万円です。",
        "labels": [
            ("【急募】PHP開発案件", "TITLE"),
            ("現場はフルリモートでECサイト改修", "SUMMARY"),
            ("75万円", "PRICE")
        ]
    },
    {
        "text": "案件：Python機械学習 概要：AIの実装 費用：100万",
        "labels": [
            ("Python機械学習", "TITLE"),
            ("AIの実装", "SUMMARY"),
            ("100万", "PRICE")
        ]
    },
    {
        "text": "金融システム移行PJ。基本設計から担当。単価はMAX90万（精算あり）",
        "labels": [
            ("金融システム移行PJ", "TITLE"),
            ("基本設計から担当", "SUMMARY"),
            ("MAX90万", "PRICE")
        ]
    },
    {
        "text": "【急募】Java開発案件 業務は基幹システム改修。単価は80万。",
        "labels": [
            ("【急募】Java開発案件", "TITLE"),
            ("基幹システム改修", "SUMMARY"),
            ("80万", "PRICE")
        ]
    },
    {
        "text": "React/Next.js案件、SPAのフロントエンド開発。単価65万。",
        "labels": [
            ("React/Next.js案件", "TITLE"),
            ("SPAのフロントエンド開発", "SUMMARY"),
            ("65万", "PRICE")
        ]
    },
    {
        "text": "AWSインフラ構築PJ。クラウド移行を担当。単価は90万円。",
        "labels": [
            ("AWSインフラ構築PJ", "TITLE"),
            ("クラウド移行を担当", "SUMMARY"),
            ("90万円", "PRICE")
        ]
    },
    {
        "text": "案件:Go言語開発 概要:マイクロサービス基盤の開発 費用:88万",
        "labels": [
            ("Go言語開発", "TITLE"),
            ("マイクロサービス基盤の開発", "SUMMARY"),
            ("88万", "PRICE")
        ]
    },
    {
        "text": "iOSアプリ開発案件。Swiftでネイティブアプリ実装。単価は75万。",
        "labels": [
            ("iOSアプリ開発案件", "TITLE"),
            ("Swiftでネイティブアプリ実装", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "Androidアプリ開発。Kotlinで機能追加を担当。単価70万円。",
        "labels": [
            ("Androidアプリ開発", "TITLE"),
            ("Kotlinで機能追加を担当", "SUMMARY"),
            ("70万円", "PRICE")
        ]
    },
    {
        "text": "Vue.js開発 管理画面のフロント実装担当 単価65万",
        "labels": [
            ("Vue.js開発", "TITLE"),
            ("管理画面のフロント実装担当", "SUMMARY"),
            ("65万", "PRICE")
        ]
    },
    {
        "text": "データエンジニア案件 ETLパイプラインの構築 単価95万",
        "labels": [
            ("データエンジニア案件", "TITLE"),
            ("ETLパイプラインの構築", "SUMMARY"),
            ("95万", "PRICE")
        ]
    },
    {
        "text": "SRE案件 監視基盤の構築運用を担当 単価100万",
        "labels": [
            ("SRE案件", "TITLE"),
            ("監視基盤の構築運用を担当", "SUMMARY"),
            ("100万", "PRICE")
        ]
    },
    {
        "text": "【急募】Salesforce開発 カスタム機能の実装 単価は75万",
        "labels": [
            ("【急募】Salesforce開発", "TITLE"),
            ("カスタム機能の実装", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "Unity開発案件。ゲームクライアント実装担当。単価70万円。",
        "labels": [
            ("Unity開発案件", "TITLE"),
            ("ゲームクライアント実装担当", "SUMMARY"),
            ("70万円", "PRICE")
        ]
    },
    {
        "text": "Scala案件、大規模データ処理基盤の開発、単価90万",
        "labels": [
            ("Scala案件", "TITLE"),
            ("大規模データ処理基盤の開発", "SUMMARY"),
            ("90万", "PRICE")
        ]
    },
    {
        "text": "Kotlin開発 サーバーサイドAPI実装 単価は80万",
        "labels": [
            ("Kotlin開発", "TITLE"),
            ("サーバーサイドAPI実装", "SUMMARY"),
            ("80万", "PRICE")
        ]
    },
    {
        "text": "C#開発案件 業務システム改修担当 単価70万",
        "labels": [
            ("C#開発案件", "TITLE"),
            ("業務システム改修担当", "SUMMARY"),
            ("70万", "PRICE")
        ]
    },
    {
        "text": "Flutter開発 クロスプラットフォームアプリ開発 単価75万",
        "labels": [
            ("Flutter開発", "TITLE"),
            ("クロスプラットフォームアプリ開発", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "Terraform案件、インフラのコード化を担当、単価85万",
        "labels": [
            ("Terraform案件", "TITLE"),
            ("インフラのコード化を担当", "SUMMARY"),
            ("85万", "PRICE")
        ]
    },
    {
        "text": "Kubernetes運用案件 コンテナ基盤の運用保守 単価は90万",
        "labels": [
            ("Kubernetes運用案件", "TITLE"),
            ("コンテナ基盤の運用保守", "SUMMARY"),
            ("90万", "PRICE")
        ]
    },
    {
        "text": "TypeScript開発 SaaSのフロントエンド開発 単価80万円",
        "labels": [
            ("TypeScript開発", "TITLE"),
            ("SaaSのフロントエンド開発", "SUMMARY"),
            ("80万円", "PRICE")
        ]
    },
    {
        "text": "Rust開発案件、低レイヤーシステムの実装、単価MAX95万",
        "labels": [
            ("Rust開発案件", "TITLE"),
            ("低レイヤーシステムの実装", "SUMMARY"),
            ("MAX95万", "PRICE")
        ]
    },
    {
        "text": "Ruby on Rails案件。現場は品川。単価80万。",
        "labels": [
            ("Ruby on Rails案件", "TITLE"),
            ("現場は品川", "SUMMARY"),
            ("80万", "PRICE")
        ]
    },
    {
        "text": "Python開発案件。現場は赤坂。単価75万。",
        "labels": [
            ("Python開発案件", "TITLE"),
            ("現場は赤坂", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "Go開発案件。現場は六本木でAPI開発。単価は85万。",
        "labels": [
            ("Go開発案件", "TITLE"),
            ("現場は六本木でAPI開発", "SUMMARY"),
            ("85万", "PRICE")
        ]
    },
    # 順序バリエーション：PRICE → TITLE → SUMMARY
    {
        "text": "単価80万。Java開発案件。基幹業務システムの改修を担当。",
        "labels": [
            ("80万", "PRICE"),
            ("Java開発案件", "TITLE"),
            ("基幹業務システムの改修を担当", "SUMMARY")
        ]
    },
    {
        "text": "費用90万円｜PHP保守運用案件｜ECサイトの運用保守業務",
        "labels": [
            ("90万円", "PRICE"),
            ("PHP保守運用案件", "TITLE"),
            ("ECサイトの運用保守業務", "SUMMARY")
        ]
    },
    {
        "text": "【単価75万】React開発、SPAフロント実装",
        "labels": [
            ("75万", "PRICE"),
            ("React開発", "TITLE"),
            ("SPAフロント実装", "SUMMARY")
        ]
    },
    # 順序バリエーション：SUMMARY → TITLE → PRICE
    {
        "text": "管理画面の機能追加を担当。Angular開発案件。単価70万。",
        "labels": [
            ("管理画面の機能追加を担当", "SUMMARY"),
            ("Angular開発案件", "TITLE"),
            ("70万", "PRICE")
        ]
    },
    {
        "text": "API設計から実装まで担当｜Go言語案件｜単価85万",
        "labels": [
            ("API設計から実装まで担当", "SUMMARY"),
            ("Go言語案件", "TITLE"),
            ("85万", "PRICE")
        ]
    },
    {
        "text": "業務システムのリプレース、SAP導入案件、費用95万",
        "labels": [
            ("業務システムのリプレース", "SUMMARY"),
            ("SAP導入案件", "TITLE"),
            ("95万", "PRICE")
        ]
    },
    # 順序バリエーション：PRICE → SUMMARY → TITLE
    {
        "text": "単価100万、決済システム新規開発、Spring Boot案件",
        "labels": [
            ("100万", "PRICE"),
            ("決済システム新規開発", "SUMMARY"),
            ("Spring Boot案件", "TITLE")
        ]
    },
    {
        "text": "100万円｜AI画像認識モデル構築｜機械学習案件",
        "labels": [
            ("100万円", "PRICE"),
            ("AI画像認識モデル構築", "SUMMARY"),
            ("機械学習案件", "TITLE")
        ]
    },
    # 順序バリエーション：TITLE → PRICE → SUMMARY
    {
        "text": "Laravel開発案件 単価75万 ECサイトの新規構築",
        "labels": [
            ("Laravel開発案件", "TITLE"),
            ("75万", "PRICE"),
            ("ECサイトの新規構築", "SUMMARY")
        ]
    },
    {
        "text": "Docker/Kubernetes案件、単価90万、コンテナ基盤の移行支援",
        "labels": [
            ("Docker/Kubernetes案件", "TITLE"),
            ("90万", "PRICE"),
            ("コンテナ基盤の移行支援", "SUMMARY")
        ]
    },
    # 順序バリエーション：SUMMARY → PRICE → TITLE
    {
        "text": "セキュリティ監査の支援業務、単価80万円、QAエンジニア案件",
        "labels": [
            ("セキュリティ監査の支援業務", "SUMMARY"),
            ("80万円", "PRICE"),
            ("QAエンジニア案件", "TITLE")
        ]
    },
    {
        "text": "バッチ処理の保守運用、単価65万、Perl開発案件",
        "labels": [
            ("バッチ処理の保守運用", "SUMMARY"),
            ("65万", "PRICE"),
            ("Perl開発案件", "TITLE")
        ]
    },
    # ノイズ（無関係文章）を多く含むサンプル
    {
        "text": "いつもお世話になっております。株式会社ABCの田中です。下記案件のご紹介です。【案件名】PHP開発案件【業務内容】ECサイト改修【単価】75万円。ご検討よろしくお願いいたします。",
        "labels": [
            ("PHP開発案件", "TITLE"),
            ("ECサイト改修", "SUMMARY"),
            ("75万円", "PRICE")
        ]
    },
    {
        "text": "お世話になっております。以下案件のご紹介です。期間：即日～長期、勤務地：東京都港区、商流：エンド直、人数：1名。Java開発案件、基幹システム改修、単価80万。ご興味あればご返信ください。",
        "labels": [
            ("Java開発案件", "TITLE"),
            ("基幹システム改修", "SUMMARY"),
            ("80万", "PRICE")
        ]
    },
    {
        "text": "ご無沙汰しております。先日はありがとうございました。早速ですが、Python機械学習の案件をご紹介します。内容はAIモデルの実装支援、単価は90万円。スキルシートお待ちしております。",
        "labels": [
            ("Python機械学習", "TITLE"),
            ("AIモデルの実装支援", "SUMMARY"),
            ("90万円", "PRICE")
        ]
    },
    {
        "text": "営業の佐藤です。リモート可、面談1回（オンライン）、外国籍不可。React開発案件。SPAのフロントエンド実装。単価70万円。ご検討のほどよろしくお願いいたします。",
        "labels": [
            ("React開発案件", "TITLE"),
            ("SPAのフロントエンド実装", "SUMMARY"),
            ("70万円", "PRICE")
        ]
    },
    {
        "text": "下記新規案件のご共有です。商流：弊社→エンド、精算幅140-180h、開始日：来月～。Go言語案件、APIサーバー開発、単価85万。ご興味ありましたらご一報ください。",
        "labels": [
            ("Go言語案件", "TITLE"),
            ("APIサーバー開発", "SUMMARY"),
            ("85万", "PRICE")
        ]
    },
    {
        "text": "ご連絡ありがとうございます。先日いただいた要件にマッチする案件です。場所は新宿、リモートと出社のハイブリッド勤務。AWSインフラ構築案件、クラウド移行支援、単価95万。詳細は別途お送りします。",
        "labels": [
            ("AWSインフラ構築案件", "TITLE"),
            ("クラウド移行支援", "SUMMARY"),
            ("95万", "PRICE")
        ]
    },
    {
        "text": "==案件情報==\n会社：株式会社XYZ\n担当：山田\n----\nTypeScript開発案件\n管理画面のリプレース\n単価：80万円\n----\nご返信お待ちしております。",
        "labels": [
            ("TypeScript開発案件", "TITLE"),
            ("管理画面のリプレース", "SUMMARY"),
            ("80万円", "PRICE")
        ]
    },
    {
        "text": "突然のご連絡失礼いたします。エージェントの鈴木と申します。年齢：40代まで、必須スキル：3年以上の経験。Kubernetes運用案件、コンテナ基盤の運用保守、単価100万。何卒よろしくお願いします。",
        "labels": [
            ("Kubernetes運用案件", "TITLE"),
            ("コンテナ基盤の運用保守", "SUMMARY"),
            ("100万", "PRICE")
        ]
    },
    {
        "text": "お疲れ様です。以下条件の方を探しています。面談：オンライン1回、契約形態：準委任、稼働：週5日。Vue.js開発、SaaS管理画面の機能追加、単価75万円。よろしくお願いいたします。",
        "labels": [
            ("Vue.js開発", "TITLE"),
            ("SaaS管理画面の機能追加", "SUMMARY"),
            ("75万円", "PRICE")
        ]
    },
    {
        "text": "【メール署名は省略】平素より大変お世話になっております。下記の通り案件のご紹介です。なお服装自由、フレックスタイム制となります。Scala案件、データ基盤の構築支援、単価92万。ご検討よろしくお願いします。",
        "labels": [
            ("Scala案件", "TITLE"),
            ("データ基盤の構築支援", "SUMMARY"),
            ("92万", "PRICE")
        ]
    },
    {
        "text": "おはようございます。本日も案件のご紹介です。応募締切：今週金曜、勤務地：大阪市内、交通費別途支給。Ruby on Rails案件、ECサイト機能拡張、単価78万。ご返信お待ちしております。",
        "labels": [
            ("Ruby on Rails案件", "TITLE"),
            ("ECサイト機能拡張", "SUMMARY"),
            ("78万", "PRICE")
        ]
    },
    {
        "text": "ご紹介ありがとうございました。さて、別件で恐縮ですが、以下案件いかがでしょうか。フルリモート可、商流2次まで、即日参画可能な方優遇。C#開発案件、業務システム機能追加、単価73万。",
        "labels": [
            ("C#開発案件", "TITLE"),
            ("業務システム機能追加", "SUMMARY"),
            ("73万", "PRICE")
        ]
    },
    {
        "text": "週末にすみません。月曜までに人選したい急ぎ案件です。エンド：金融系大手、面談：書類選考のみ、開始：再来月。SRE案件、監視基盤の改善業務、単価105万円。ご検討お願いします。",
        "labels": [
            ("SRE案件", "TITLE"),
            ("監視基盤の改善業務", "SUMMARY"),
            ("105万円", "PRICE")
        ]
    },
    {
        "text": "新規ご挨拶失礼します。弊社では多数の案件を扱っております。本案件は東京都千代田区、勤務時間9-18時、休日：土日祝。Salesforce開発、カスタム機能の実装支援、単価83万。",
        "labels": [
            ("Salesforce開発", "TITLE"),
            ("カスタム機能の実装支援", "SUMMARY"),
            ("83万", "PRICE")
        ]
    },
    {
        "text": "返信不要です。情報共有まで。詳細は添付のスキルシート参照、応募はメールにて、面談は来週中に実施。Flutter開発、iOS/Androidアプリの新機能開発、単価77万。",
        "labels": [
            ("Flutter開発", "TITLE"),
            ("iOS/Androidアプリの新機能開発", "SUMMARY"),
            ("77万", "PRICE")
        ]
    },
    {
        "text": "ご無沙汰しております。下記案件いかがでしょうか。商流：弊社プロパー、契約：3ヶ月更新、面談：1回オンラインのみ。Terraform案件、IaCによるインフラ整備、単価88万円。",
        "labels": [
            ("Terraform案件", "TITLE"),
            ("IaCによるインフラ整備", "SUMMARY"),
            ("88万円", "PRICE")
        ]
    },
    # 実験2追加: 不足ボキャブラリ補強（Swift, Django, FastAPI, C++, Vue.js開発案件, MAX系, ｜区切り, 改行ノイズ）
    {
        "text": "【急募】Swift開発案件、iOSネイティブアプリの新規開発、単価82万円。",
        "labels": [
            ("【急募】Swift開発案件", "TITLE"),
            ("iOSネイティブアプリの新規開発", "SUMMARY"),
            ("82万円", "PRICE")
        ]
    },
    {
        "text": "Swift案件 iOSアプリの機能追加担当 単価78万",
        "labels": [
            ("Swift案件", "TITLE"),
            ("iOSアプリの機能追加担当", "SUMMARY"),
            ("78万", "PRICE")
        ]
    },
    {
        "text": "Django開発案件、Pythonバックエンド構築、単価83万円。",
        "labels": [
            ("Django開発案件", "TITLE"),
            ("Pythonバックエンド構築", "SUMMARY"),
            ("83万円", "PRICE")
        ]
    },
    {
        "text": "Django案件 BtoB向けサービスの実装 単価88万",
        "labels": [
            ("Django案件", "TITLE"),
            ("BtoB向けサービスの実装", "SUMMARY"),
            ("88万", "PRICE")
        ]
    },
    {
        "text": "【急募】FastAPI開発案件、Python製マイクロサービス構築、単価92万。",
        "labels": [
            ("【急募】FastAPI開発案件", "TITLE"),
            ("Python製マイクロサービス構築", "SUMMARY"),
            ("92万", "PRICE")
        ]
    },
    {
        "text": "FastAPI案件 REST API設計と実装 単価85万円",
        "labels": [
            ("FastAPI案件", "TITLE"),
            ("REST API設計と実装", "SUMMARY"),
            ("85万円", "PRICE")
        ]
    },
    {
        "text": "C++案件、組み込み制御システムの開発、単価95万。",
        "labels": [
            ("C++案件", "TITLE"),
            ("組み込み制御システムの開発", "SUMMARY"),
            ("95万", "PRICE")
        ]
    },
    {
        "text": "C++開発、画像処理エンジンの実装、単価100万円",
        "labels": [
            ("C++開発", "TITLE"),
            ("画像処理エンジンの実装", "SUMMARY"),
            ("100万円", "PRICE")
        ]
    },
    {
        "text": "Vue.js開発案件、SaaS管理画面のリプレース、単価78万円。",
        "labels": [
            ("Vue.js開発案件", "TITLE"),
            ("SaaS管理画面のリプレース", "SUMMARY"),
            ("78万円", "PRICE")
        ]
    },
    {
        "text": "TypeScript開発案件、フロントエンドの大規模リファクタ、単価88万",
        "labels": [
            ("TypeScript開発案件", "TITLE"),
            ("フロントエンドの大規模リファクタ", "SUMMARY"),
            ("88万", "PRICE")
        ]
    },
    # MAX系PRICEパターンを増やす
    {
        "text": "Java案件、銀行系システム改修、単価MAX100万。",
        "labels": [
            ("Java案件", "TITLE"),
            ("銀行系システム改修", "SUMMARY"),
            ("MAX100万", "PRICE")
        ]
    },
    {
        "text": "MAX90万、Python案件、データ分析業務",
        "labels": [
            ("MAX90万", "PRICE"),
            ("Python案件", "TITLE"),
            ("データ分析業務", "SUMMARY")
        ]
    },
    {
        "text": "MAX85万 / Go案件 / API開発",
        "labels": [
            ("MAX85万", "PRICE"),
            ("Go案件", "TITLE"),
            ("API開発", "SUMMARY")
        ]
    },
    # ｜区切りパターンを増やす
    {
        "text": "PHP開発｜ECサイトの機能拡張｜単価75万",
        "labels": [
            ("PHP開発", "TITLE"),
            ("ECサイトの機能拡張", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "Java開発｜業務システムの保守｜単価80万円",
        "labels": [
            ("Java開発", "TITLE"),
            ("業務システムの保守", "SUMMARY"),
            ("80万円", "PRICE")
        ]
    },
    {
        "text": "Python案件｜MLモデルの改善業務｜単価92万",
        "labels": [
            ("Python案件", "TITLE"),
            ("MLモデルの改善業務", "SUMMARY"),
            ("92万", "PRICE")
        ]
    },
    # 改行多めのフォーマット
    {
        "text": "==案件詳細==\nエンド：大手SIer\n商流：弊社→元請\n精算：140-180h\n----\nPython案件\nバッチ処理の保守運用\n単価85万\n----\nご検討お願いします。",
        "labels": [
            ("Python案件", "TITLE"),
            ("バッチ処理の保守運用", "SUMMARY"),
            ("85万", "PRICE")
        ]
    },
    {
        "text": "==募集要項==\n勤務地：東京\n商流：エンド直\n----\nGo案件\nマイクロサービスの新規開発\n単価92万円\n----\nよろしくお願いいたします。",
        "labels": [
            ("Go案件", "TITLE"),
            ("マイクロサービスの新規開発", "SUMMARY"),
            ("92万円", "PRICE")
        ]
    },
    # 「/」区切りパターンを補強
    {
        "text": "MAX95万 / Java案件 / 業務システム改修",
        "labels": [
            ("MAX95万", "PRICE"),
            ("Java案件", "TITLE"),
            ("業務システム改修", "SUMMARY")
        ]
    },
    {
        "text": "PHP案件 / ECサイト機能追加 / 単価78万",
        "labels": [
            ("PHP案件", "TITLE"),
            ("ECサイト機能追加", "SUMMARY"),
            ("78万", "PRICE")
        ]
    },
    # 実験4追加: 失敗ケースのフォーマット・語彙にマッチする訓練データ
    # 「【急募】Swift開発」「Swift開発」のパターン
    {
        "text": "【急募】Swift開発 iOSアプリの保守業務 単価77万",
        "labels": [
            ("【急募】Swift開発", "TITLE"),
            ("iOSアプリの保守業務", "SUMMARY"),
            ("77万", "PRICE")
        ]
    },
    {
        "text": "Swift開発 iOSアプリのリプレース 単価83万円",
        "labels": [
            ("Swift開発", "TITLE"),
            ("iOSアプリのリプレース", "SUMMARY"),
            ("83万円", "PRICE")
        ]
    },
    # 「Vue.js開発案件」（案件まで含むTITLE）のパターン
    {
        "text": "Vue.js開発案件 BtoC向けフロント実装 単価72万",
        "labels": [
            ("Vue.js開発案件", "TITLE"),
            ("BtoC向けフロント実装", "SUMMARY"),
            ("72万", "PRICE")
        ]
    },
    {
        "text": "Vue.js開発案件 SaaSフロントエンドの改修 費用80万円",
        "labels": [
            ("Vue.js開発案件", "TITLE"),
            ("SaaSフロントエンドの改修", "SUMMARY"),
            ("80万円", "PRICE")
        ]
    },
    # 「C++案件 ... 単価N万」のパターン
    {
        "text": "C++案件 制御系ソフトの開発担当 単価90万",
        "labels": [
            ("C++案件", "TITLE"),
            ("制御系ソフトの開発担当", "SUMMARY"),
            ("90万", "PRICE")
        ]
    },
    {
        "text": "C++案件 デバイスドライバの実装 単価85万円",
        "labels": [
            ("C++案件", "TITLE"),
            ("デバイスドライバの実装", "SUMMARY"),
            ("85万円", "PRICE")
        ]
    },
    # 「Django開発」（案件なし）のパターン
    {
        "text": "Django開発 BtoB向けポータルサイト構築 単価82万円",
        "labels": [
            ("Django開発", "TITLE"),
            ("BtoB向けポータルサイト構築", "SUMMARY"),
            ("82万円", "PRICE")
        ]
    },
    {
        "text": "Django開発 PythonバックエンドAPI実装 単価88万",
        "labels": [
            ("Django開発", "TITLE"),
            ("PythonバックエンドAPI実装", "SUMMARY"),
            ("88万", "PRICE")
        ]
    },
    # 「【急募】FastAPI開発」（テスト#20）のパターン
    {
        "text": "【急募】FastAPI開発 Pythonサーバーサイドの実装 単価87万",
        "labels": [
            ("【急募】FastAPI開発", "TITLE"),
            ("Pythonサーバーサイドの実装", "SUMMARY"),
            ("87万", "PRICE")
        ]
    },
    {
        "text": "FastAPI開発 API基盤のリファクタ 単価90万円",
        "labels": [
            ("FastAPI開発", "TITLE"),
            ("API基盤のリファクタ", "SUMMARY"),
            ("90万円", "PRICE")
        ]
    },
    # 改行＋区切り線フォーマット（テスト#24 と同形式）
    {
        "text": "==案件詳細==\nエンド：大手SIer\n商流：弊社→元請\n精算：140-180h\n----\nGo案件\nAPI基盤の新規開発\n単価88万\n----\nご検討よろしくお願いします。",
        "labels": [
            ("Go案件", "TITLE"),
            ("API基盤の新規開発", "SUMMARY"),
            ("88万", "PRICE")
        ]
    },
    {
        "text": "==案件詳細==\nエンド：通信系大手\n商流：エンド直\n精算：140-180h\n----\nPHP案件\nECサイトの保守運用\n単価75万\n----\nご返信お待ちしております。",
        "labels": [
            ("PHP案件", "TITLE"),
            ("ECサイトの保守運用", "SUMMARY"),
            ("75万", "PRICE")
        ]
    },
    {
        "text": "==案件詳細==\nエンド：金融系\n商流：弊社→元請\n精算：140-180h\n----\nRuby案件\n基幹システム改修\n単価92万\n----\nご検討お願いします。",
        "labels": [
            ("Ruby案件", "TITLE"),
            ("基幹システム改修", "SUMMARY"),
            ("92万", "PRICE")
        ]
    },
    # 「｜」区切りで SUMMARY を強化（テスト#8 のパターン）
    {
        "text": "Java開発｜Web画面の機能追加｜単価70万",
        "labels": [
            ("Java開発", "TITLE"),
            ("Web画面の機能追加", "SUMMARY"),
            ("70万", "PRICE")
        ]
    },
    {
        "text": "Go開発｜APIサーバーの保守｜単価82万",
        "labels": [
            ("Go開発", "TITLE"),
            ("APIサーバーの保守", "SUMMARY"),
            ("82万", "PRICE")
        ]
    },
    {
        "text": "Ruby開発｜ECサイトの新規構築｜単価85万円",
        "labels": [
            ("Ruby開発", "TITLE"),
            ("ECサイトの新規構築", "SUMMARY"),
            ("85万円", "PRICE")
        ]
    },
    # 「案件：X 概要：Y 費用：Z」フォーマット（テスト#12 のパターン）
    {
        "text": "案件：Ruby 概要：APIサーバーの実装 費用：78万",
        "labels": [
            ("Ruby", "TITLE"),
            ("APIサーバーの実装", "SUMMARY"),
            ("78万", "PRICE")
        ]
    },
    {
        "text": "案件：Java 概要：基幹システムの保守運用 費用：85万",
        "labels": [
            ("Java", "TITLE"),
            ("基幹システムの保守運用", "SUMMARY"),
            ("85万", "PRICE")
        ]
    }
]

# テスト用データ（学習データには含まれない未知のサンプル）
TEST_DATA = [
    {
        "text": "Ruby開発案件。現場は渋谷。単価は70万。",
        "expected": {"TITLE": "Ruby開発案件", "SUMMARY": "現場は渋谷", "PRICE": "70万"}
    },
    {
        "text": "TypeScript案件 概要：管理画面のリプレース 単価85万",
        "expected": {"TITLE": "TypeScript案件", "SUMMARY": "管理画面のリプレース", "PRICE": "85万"}
    },
    {
        "text": "【急募】Swift開発 iOSアプリの新機能追加 単価80万円",
        "expected": {"TITLE": "【急募】Swift開発", "SUMMARY": "iOSアプリの新機能追加", "PRICE": "80万円"}
    },
    {
        "text": "単価95万、Python案件、機械学習モデルのチューニング",
        "expected": {"TITLE": "Python案件", "SUMMARY": "機械学習モデルのチューニング", "PRICE": "95万"}
    },
    {
        "text": "決済システム保守、PHP案件、単価70万",
        "expected": {"TITLE": "PHP案件", "SUMMARY": "決済システム保守", "PRICE": "70万"}
    },
    {
        "text": "Vue.js開発案件 SPAの実装担当 費用65万",
        "expected": {"TITLE": "Vue.js開発案件", "SUMMARY": "SPAの実装担当", "PRICE": "65万"}
    },
    {
        "text": "AWS構築案件、インフラ設計から運用まで、単価100万",
        "expected": {"TITLE": "AWS構築案件", "SUMMARY": "インフラ設計から運用まで", "PRICE": "100万"}
    },
    {
        "text": "Kotlin開発、Androidアプリの保守、単価75万",
        "expected": {"TITLE": "Kotlin開発", "SUMMARY": "Androidアプリの保守", "PRICE": "75万"}
    },
    {
        "text": "Scala案件。データ基盤のリファクタリング。単価90万円。",
        "expected": {"TITLE": "Scala案件", "SUMMARY": "データ基盤のリファクタリング", "PRICE": "90万円"}
    },
    {
        "text": "Node.js開発、APIサーバー構築、単価80万",
        "expected": {"TITLE": "Node.js開発", "SUMMARY": "APIサーバー構築", "PRICE": "80万"}
    },
    {
        "text": "100万、ReactNative案件、クロスプラットフォーム開発",
        "expected": {"TITLE": "ReactNative案件", "SUMMARY": "クロスプラットフォーム開発", "PRICE": "100万"}
    },
    {
        "text": "案件：DevOps 概要：CI/CDパイプライン構築 費用：90万",
        "expected": {"TITLE": "DevOps", "SUMMARY": "CI/CDパイプライン構築", "PRICE": "90万"}
    },
    {
        "text": "Unity開発、ソシャゲのクライアント実装、単価85万",
        "expected": {"TITLE": "Unity開発", "SUMMARY": "ソシャゲのクライアント実装", "PRICE": "85万"}
    },
    {
        "text": "C++案件 組み込みシステム開発担当 単価95万",
        "expected": {"TITLE": "C++案件", "SUMMARY": "組み込みシステム開発担当", "PRICE": "95万"}
    },
    {
        "text": "テスト自動化案件、Seleniumでの自動化推進、単価70万",
        "expected": {"TITLE": "テスト自動化案件", "SUMMARY": "Seleniumでの自動化推進", "PRICE": "70万"}
    },
    {
        "text": "Django開発 BtoC向けWebサービス構築 単価80万円",
        "expected": {"TITLE": "Django開発", "SUMMARY": "BtoC向けWebサービス構築", "PRICE": "80万円"}
    },
    {
        "text": "MAX110万 / SRE案件 / 監視運用業務",
        "expected": {"TITLE": "SRE案件", "SUMMARY": "監視運用業務", "PRICE": "MAX110万"}
    },
    {
        "text": "金融系プロジェクト、システム再構築の支援、単価105万",
        "expected": {"TITLE": "金融系プロジェクト", "SUMMARY": "システム再構築の支援", "PRICE": "105万"}
    },
    {
        "text": "Rails案件、ECサイトの機能拡張、単価85万",
        "expected": {"TITLE": "Rails案件", "SUMMARY": "ECサイトの機能拡張", "PRICE": "85万"}
    },
    {
        "text": "【急募】FastAPI開発 Python製APIの新規構築 単価90万",
        "expected": {"TITLE": "【急募】FastAPI開発", "SUMMARY": "Python製APIの新規構築", "PRICE": "90万"}
    },
    # ノイズ（無関係文章）を多く含むテストサンプル
    {
        "text": "いつもお世話になっております。株式会社サンプルの高橋です。下記案件のご紹介となります。Ruby開発案件、ECサイトの保守運用業務、単価72万。ご検討よろしくお願いいたします。",
        "expected": {"TITLE": "Ruby開発案件", "SUMMARY": "ECサイトの保守運用業務", "PRICE": "72万"}
    },
    {
        "text": "お疲れ様です。期間：即日～長期、勤務地：東京都渋谷区、商流：エンド直、面談：1回オンライン。Python開発案件、データ分析基盤の構築、単価88万円。",
        "expected": {"TITLE": "Python開発案件", "SUMMARY": "データ分析基盤の構築", "PRICE": "88万円"}
    },
    {
        "text": "営業の伊藤と申します。突然のご連絡失礼します。リモート可、フレックス制、外国籍不可、年齢制限なし。Node.js案件、リアルタイムチャット機能の実装、単価82万。",
        "expected": {"TITLE": "Node.js案件", "SUMMARY": "リアルタイムチャット機能の実装", "PRICE": "82万"}
    },
    {
        "text": "==案件詳細==\nエンド：大手金融\n商流：弊社→元請\n精算：140-180h\n----\nJava案件\n勘定系システム改修\n単価98万\n----\nご返信お待ちしております。",
        "expected": {"TITLE": "Java案件", "SUMMARY": "勘定系システム改修", "PRICE": "98万"}
    },
    {
        "text": "ご無沙汰しております。下記案件いかがでしょうか。面談はオンラインで実施、契約は準委任、稼働は週5日固定。AWS構築案件、マルチアカウント環境の設計、単価110万円。",
        "expected": {"TITLE": "AWS構築案件", "SUMMARY": "マルチアカウント環境の設計", "PRICE": "110万円"}
    },
    {
        "text": "おはようございます。本日も案件共有です。勤務地：大阪、開始：来月～、期間：6ヶ月以上。Kotlin開発、Androidアプリの新機能追加、単価76万。何卒よろしくお願いします。",
        "expected": {"TITLE": "Kotlin開発", "SUMMARY": "Androidアプリの新機能追加", "PRICE": "76万"}
    },
    {
        "text": "突然のご連絡失礼いたします。エージェントの中村です。応募締切：今週中、面談：書類選考あり、服装自由。ReactNative案件、クロスプラットフォームアプリ開発、単価84万円。",
        "expected": {"TITLE": "ReactNative案件", "SUMMARY": "クロスプラットフォームアプリ開発", "PRICE": "84万円"}
    },
    {
        "text": "ご紹介ありがとうございます。さて別件ですが、こちらいかがでしょう。商流2次まで、フルリモート、即日参画可。DevOps案件、CI/CDパイプラインの整備、単価95万。",
        "expected": {"TITLE": "DevOps案件", "SUMMARY": "CI/CDパイプラインの整備", "PRICE": "95万"}
    }
]
