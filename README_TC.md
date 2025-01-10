# 🤖💡 LangOllamaQ(深藍)

<div align="center">

簡體中文 / [繁體中文](README_TC.md) / [English](README.md) / [Deutsch](README_DE.md) / [日本語](README_JP.md)
</div>

---

## 🌐 專案概述 <span style="color: #2ecc71;">Project Overview</span>
LangOllamaQ 是一款結合了先進技術的本地知識庫問答系統，基於 🤖 <span style="color: #e74c3c;">LangChain</span> 和 📚 <span style="color: #e74c3c;">Ollama模型框架</span> 建構。它能夠輕鬆加載本地資料夾中的多個文件，生成嵌入並存儲在向量數據庫中，實現基於文件上下文的問答功能，並記錄對話歷史，構建持續互動的 AI 語義搜索助手。🔍📚
### 功能亮點 <span style="color: #f1c40f;">Features</span>
- **多文件支持**：遞歸掃描資料夾，加載所有 PDF 文件。📁
- **高效向量存儲**：使用 Ollama 嵌入模型生成文本向量並存儲，支持基於內容的**高效檢索**。🔍
- **語義問答功能**：結合上下文生成精確且符合語境的答案。💬
- **記憶模塊**：記錄使用者對話歷史，支持動態查詢、更新和清除。💾
- **可擴展性**：輕鬆集成其他文件類型（如 .txt、.docx）或持久化向量存儲方案。🔧
> 💡 <span style="color: #f1c40f;">**注意**</span>：本產品目前處於測試階段，提供的知識庫內容僅供測試使用。在實際環境中部署產品時，使用者需要根據需要融入行業特定的知識。
### 專案結構 <span style="color: #9b59b6;">Project Structure</span>
```plaintext
LangOllamaQ/
├── documents/
│   # 儲存所有 PDF 文件
├── loader/
│   └── pdf_loader.py
│       # 掃描和加載資料夾中的文件
├── embeddings/
│   └── generate_embeddings.py
│       # 生成向量嵌入並存儲
├── qa/
│   └── qa_with_context.py
│       # 基於上下文生成回答
├── memory/
│   └── memory_manager.py
│       # 記錄和管理使用者對話歷史
├── main.py
│   # 主程式入口
├── requirements.txt
│   # 依賴文件
├── .gitignore
│   # 忽略文件
└── README.md
    # 專案說明文件
```
### 快速上手 <span style="color: #e67e22;">Quick Start</span>
#### 克隆專案 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### 安裝依賴 📦
推薦使用虛擬環境管理依賴：
#### 創建虛擬環境
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
## 安裝依賴
```bash
pip install -r requirements.txt
```
## 添加文件 📄
將你的 PDF 文件添加到 `documents/` 資料夾下。
## 執行程式 🚀
```bash
python main.py
```
程式會自動加載 `documents/` 資料夾中的所有 PDF 文件，生成向量嵌入，並進入互動式問答模式。
## 特殊指令 <span style="color: #1abc9c;">Special Commands</span>
- 退出程式：輸入 `q` 🚪
- 清除記憶：輸入 `clear` 🧼
## 模組設計 <span style="color: #3498db;">Module Design</span>
### 文件加載模組 (loader/pdf_loader.py)
```
負責遞歸掃描指定資料夾並加載所有 PDF 文件內容。支持大文件分頁加載。
核心函數：`load_documents_from_folder(folder_path)`
```
### 嵌入生成模組 (embeddings/generate_embeddings.py)
```
使用 Ollama 的嵌入模型生成向量表示，並存儲在記憶體向量數據庫中。
核心函數：`generate_embeddings(docs)`
```
### 問答模組 (qa/qa_with_context.py)
```
基於使用者提問，從向量數據庫中檢索相關上下文，生成回答。
```
### 記憶模塊（memory/memory_manager.py）
```
記錄使用者的提問和回答歷史，支持上下文關聯以及記憶清除。
核心函數：
add_to_memory(question, answer)
get_full_memory()
clear_memory()
```
## 🌟 示例使用
## 加載文件並生成回答
假設你有以下提問：
```
> 請你簡單總結一下各文件的内容
```
程式會從加載的文件中檢索相關上下文，並生成以下回答：
```
> 深藍: 這段文本主要討論了圖神經網絡（GNNs）在處理圖形數據時遇到的挑戰，特別是關於如何通過幾何增強來提高其表現力。以下是幾個關鍵點：
1. **訓練過程中的問題**：圖神經網絡在訓練過程中會面臨過平滑（over-smoothing）和過度擠壓（over-squashing）的問題。這些問題是由於網絡深度增加導致節點表示變得無法區分或重要信息被壓縮所引起的。
2. **通過重構來解決這些問題**：一種緩解方法是使用基於圖形離散曲率的預處理技術，即“重連”過程。這種方法在高曲率區域移除邊，在低曲率區域添加新邊，以減少過平滑和過度擠壓的影響。
3. **圖神經網絡的學習能力限制**：標準消息傳遞機制的GNNs不能學到如果兩幅圖像拓撲不同，則它們表示不同的映射關係。這意味著GNNs可能無法學習某些基本功能，如計算圖形直徑或確定最大环路大小。
4. **增強表現力的方法**：為了提高圖神經網絡的表現能力，可以通過增加幾何信息來豐富節點表示，例如使用拉普拉斯譜（Laplacian spectrum）和離散曲率。這些技術能夠幫助GNNs學習更多關於圖形的結構信息。       
5. **基於離散曲率的信息捕獲方式**：離散曲率可以捕捉到一個節點兩跳鄰居內的局部結構信息，而消息傳遞機制只能獲取一跳鄰域內的信息。
總之，本文討論了圖神經網絡如何利用幾何增強技術來克服現有的局限性，並提高其在圖形數據處理上的能力。這些方法為解決GNNs的過平滑和過度擠壓問題提供了一種有效途徑，同時也有助於增強節點表示的學習過程，使之更適合下游任務的應用需求。
```
## 對話歷史記錄
使用者可以在多輪對話中保留上下文：
```
你：曙光萬物團隊的核心業務是什麼？
深藍：曙光萬物團隊的核心業務是推動人工智慧技術在教育、醫療和工業領域的應用，通過深度學習和機器學習技術解決實際問題。
你：那他們有什麼具體的產品或服務嗎？
深藍：曙光萬物團隊推出了多款產品，包括智能教育輔助系統、智能醫療診斷系統和工業自動化解決方案。
你：這些產品在市場上的反應如何？
深藍：這些產品在市場上受到了廣泛好評，特別是智能教育輔助系統，它在提高學習效率和教學質量方面表現突出。
```
## 贡献指南
コントリビューションを歓迎します。コードの寄付、バグの報告、機能要求の提出をお待ちしています！
## ライセンス
このプロジェクトはGPL-3.0ライセンスでオープンソース化されており、自由に使用・修正できます。
---
このマークダウンコードは、LangOllamaQ(深蓝)のREADMEファイルを日本語に翻訳したものです。連続性を保ちつつ、必要な情報を伝えるようにしています。
