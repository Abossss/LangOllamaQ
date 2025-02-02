# 🤖💡 LangOllamaQ(深蓝)

<div align="center">

[简体中文](README_CN.md) / [繁体中文](README_TC.md) / [English](README.md) / [Deutsch](README_DE.md) / 日本語

</div>

---

## 🌐 プロジェクト概要 <span style="color: #2ecc71;">Project Overview</span>
LangOllamaQは、先端技術を結合したローカルな知識ベースのQ&Aシステムで、🤖 <span style="color: #e74c3c;">LangChain</span>と📚 <span style="color: #e74c3c;">Ollamaモデルフレームワーク</span>を基に構築されています。このシステムは、ローカルフォルダー内の複数のドキュメントを簡単に読み込み、埋め込みを生成し、ベクトルデータベースに保存し、ドキュメントのコンテキストに基づいたQ&A機能を実現し、対話履歴を記録し、継続的なインタラクションをサポートするAIセマンティック検索アシスタントを構築します。🔍📚
### 機能のハイライト <span style="color: #f1c40f;">Features</span>
- **複数のドキュメントサポート**：フォルダーを再帰的にスキャンし、すべてのPDFドキュメントを読み込みます。📁
- **効率的なベクトル保存**：Ollamaの埋め込みモデルを使用してテキストベクトルを生成し、保存し、コンテンツに基づく**効率的な検索**をサポートします。🔍
- **セマンティックQ&A機能**：コンテキストと組み合わせて正確で文脈に合った答えを生成します。💬
- **記憶モジュール**：ユーザーの対話履歴を記録し、動的なクエリ、更新、クリアをサポートします。💾
- **拡張性**：他のドキュメントタイプ（.txt、.docxなど）を簡単に統合したり、永続的なベクトル保存ソリューションを統合することができます。🔧
> 💡 <span style="color: #f1c40f;">**注意**</span>：この製品は現在テスト段階であり、提供される知識ベースコンテンツはテスト用です。実際の環境で製品をデプロイする際には、ユーザーは必要に応じて業界固有の知識を組み込む必要があります。
### プロジェクト構造 <span style="color: #9b59b6;">Project Structure</span>
```plaintext
LangOllamaQ/
├── documents/
│   # すべてのPDFドキュメントを保存
├── loader/
│   └── pdf_loader.py
│       # フォルダー内のドキュメントをスキャンして読み込み
├── embeddings/
│   └── generate_embeddings.py
│       # 埋め込みを生成し、保存
├── qa/
│   └── qa_with_context.py
│       # コンテキストに基づいて回答を生成
├── memory/
│   └── memory_manager.py
│       # ユーザーの対話履歴を記録し、管理
├── main.py
│   # メインプログラムのエントリーポイント
├── requirements.txt
│   # 依存ファイル
├── .gitignore
│   # ファイルを無視する
└── README.md
    # プロジェクト説明書
```
### クイックスタート <span style="color: #e67e22;">Quick Start</span>

#### プロジェクトをクローン 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### クイックスタート <span style="color: #e67e22;">Quick Start</span>
#### プロジェクトをクローン 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### 依存関係をインストール 📦
仮想環境を使用して依存関係を管理することを推奨します：
#### 仮想環境を作成
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
## 依存関係をインストール
```bash
pip install -r requirements.txt
```
## ドキュメントを追加 📄
PDF ファイルを `documents/` フォルダーに追加してください。
## プログラムを実行 🚀
```bash
python main.py
```
プログラムは `documents/` フォルダー内のすべての PDF ファイルを自動で読み込み、ベクトル埋め込みを生成し、対話型の Q&A モードに入ります。
## 特殊コマンド <span style="color: #1abc9c;">Special Commands</span>
- プログラムを終了する：`q` を入力 🚪
- 記憶をクリアする：`clear` を入力 🧼
## モジュール設計 <span style="color: #3498db;">Module Design</span>
### ドキュメントロードモジュール (loader/pdf_loader.py)
```
指定されたフォルダーを再帰的にスキャンし、すべての PDF ドキュメントを読み込みます。大きなファイルのページ分割読込みをサポートします。
主要な関数：`load_documents_from_folder(folder_path)`
```
### 埋め込み生成モジュール (embeddings/generate_embeddings.py)
```
Ollama の埋め込みモデルを使用してベクトル表現を生成し、メモリ内のベクトルデータベースに保存します。
主要な関数：`generate_embeddings(docs)`
```
### Q&A モジュール (qa/qa_with_context.py)
```
ユーザーの質問に基づいて、ベクトルデータベースから関連するコンテキストを検索し、回答を生成します。
```
### 記憶モジュール（memory/memory_manager.py）
```
ユーザーの質問と回答の履歴を記録し、コンテキスト関連付けと記憶クリアをサポートします。
主要な関数：
add_to_memory(question, answer)
get_full_memory()
clear_memory()
```
## 🌟 使用例
## ドキュメントをロードして回答を生成
以下のような質問があったとします：
```
> 各ドキュメントの内容を簡単にまとめてください
```
プログラムはロードしたドキュメントから関連するコンテキストを検索し、以下のような回答を生成します：
```
> 深蓝: このテキストは、グラフニューラルネットワーク（GNNs）がグラフデータを処理する際に直面する課題について議論しています。特に、ジオメトリの強化を通じてその表現力を向上させる方法についてです。以下に几个のキーポイントを挙げます：

1. **トレーニングプロセスの問題**：グラフニューラルネットワークはトレーニング中にオーバースムージング（over-smoothing）とオーバースクラッシュ（over-squashing）の問題に直面します。これらの問題は、ネットワークの深さが増加することでノードの表現が区別がつかなくなったり、重要な情報が圧縮されたりすることに起因しています。

2. **これらの問題を解決するための再構築**：これらの問題を緩和する一つの方法は、グラフの離散曲率に基づく前処理技術、すなわち「リンク再構築」プロセスを使用することです。この方法は、高曲率領域でエッジを削除し、低曲率領域で新しいエッジを追加することで、オーバースムージングとオーバースクラッシュの影響を減少させます。

3. **グラフニューラルネットワークの学習能力の限界**：標準的なメッセージパスングメカニズムを持つGNNsは、2つの画像がトポロジー的に異なる場合、それらが異なるマッピング関係を表すことを学習することができません。これは、GNNsがグラフの直径を計算したり、最大のループサイズを決定するなどの基本的な機能を学習できない可能性を意味します。

4. **表現力を向上させる方法**：グラフニューラルネットワークの表現力を向上させるためには、ジオメトリ情報を追加してノードの表現を豊富にすることができます。例えば、ラプラシアンスペクトル（Laplacian spectrum）と離散曲率を使用することです。これらの技術は、GNNsがグラフの構造情報についてより多く学習する手助けをします。

5. **離散曲率に基づく情報のキャプチャ方法**：離散曲率は、ノードの2跳以内の近傍の局所的な構造情報を捉えることができますが、メッセージパスングメカニズムは1跳の近傍の情報しか取得することができません。

以上の通り、この論文はグラフニューラルネットワークがジオメトリの強化技術をどのように使用して現存の限界を克服し、グラフデータ処理の能力を向上させるかについて議論しています。これらの方法は、GNNsのオーバースムージングとオーバースクラッシュの問題を解決するための
```

## 対話履歴記録
ユーザーは複数のラウンドの対話でコンテキストを保持することができます：
```
あなた：曙光万物チームのコアビジネスは何ですか？
深蓝：曙光万物チームのコアビジネスは、人工知能技術を教育、医療、工業に応用することです。
```
```
あなた：彼らの目標は何ですか？
深蓝：曙光万物チームは、新世代の技術人材を育成し、技術革新を推進することに専念しています。
```
ユーザーが `clear` を入力すると、記憶が消去されます：
```
あなた：clear
深蓝：対話履歴が消去されました。
```
ユーザーが `q` を入力すると、プログラムを終了します
```
あなた：q
（ここでプログラムが終了しているため、出力はありません）
```
## 🛠️ 技術スタック
- プログラミング言語：**Python >= 3.8**
- モデル：**Ollama Embeddings**, **Ollama LLM**
- フレームワーク：**LangChain**
- データベース：メモリ内ベクターストレージ（**Pinecone**、**Weaviate** などに拡張可能）
## 📖 拡張機能
- **他のドキュメント形式のサポート**：
  - 現在は **PDF** のみサポートしていますが、将来的には **.txt**、**.docx** などの形式にも拡張可能です。
- **永続化ベクターストレージ**：
  - 現在はメモリ内ストレージを使用していますが、**SQLite**、**Pinecone** などに基づく永続化ストレージに拡張することを推奨します。
- **APIの統合**：
  - **RESTful** や **gRPC** インターフェースを追加することで、フロントエンドや他のシステムとの統合を容易にします。
- **クラウドデプロイメント**：
  - **AWS**、**GCP**、**Azure** などにデプロイして、企業レベルの知識ベースを構築することができます。
- **多言語サポート**：
  - 現在のデフォルト回答は **中国語** ですが、多言語対話にも拡張可能です。
## 🤝 貢献ガイドライン
コードの貢献、バグの報告、機能要件の提出を歓迎します！
## 📜 ライセンス
このプロジェクトは **GPL-3.0 license** に基づいてオープンソース化されており、自由に使用・修正できます。
