# 🤖💡 LangOllamaQ(深蓝)

<div align="center">

简体中文 / [繁体中文](README_TC.md) / [English](README.md) / [Deutsch](README_DE.md) / [日本語](README_JP.md)

</div>

---

## 🌐 项目概述 <span style="color: #2ecc71;">Project Overview</span>

LangOllamaQ 是一款结合了先进技术的本地知识库问答系统，基于 🤖 <span style="color: #e74c3c;">LangChain</span> 和 📚 <span style="color: #e74c3c;">Ollama模型框架</span> 构建。它能够轻松加载本地文件夹中的多个文档，生成嵌入并存储在向量数据库中，实现基于文档上下文的问答功能，并记录对话历史，构建持续交互的 AI 语义搜索助手。🔍📚

### 功能亮点 <span style="color: #f1c40f;">Features</span>

- **多文档支持**：递归扫描文件夹，加载所有 PDF 文档。📁
- **高效向量存储**：使用 Ollama 嵌入模型生成文本向量并存储，支持基于内容的**高效检索**。🔍
- **语义问答功能**：结合上下文生成精确且符合语境的答案。💬
- **记忆模块**：记录用户对话历史，支持动态查询、更新和清除。💾
- **可扩展性**：轻松集成其他文档类型（如 .txt、.docx）或持久化向量存储方案。🔧

> 💡 <span style="color: #f1c40f;">**注意**</span>：本产品目前处于测试阶段，提供的知识库内容仅供测试使用。在实际环境中部署产品时，用户需要根据需要融入行业特定的知识。

### 项目结构 <span style="color: #9b59b6;">Project Structure</span>

```plaintext
LangOllamaQ/
├── documents/
│   # 存储所有 PDF 文档
├── loader/
│   └── pdf_loader.py
│       # 扫描和加载文件夹中的文档
├── embeddings/
│   └── generate_embeddings.py
│       # 生成向量嵌入并存储
├── qa/
│   └── qa_with_context.py
│       # 基于上下文生成回答
├── memory/
│   └── memory_manager.py
│       # 记录和管理用户对话历史
├── main.py
│   # 主程序入口
├── requirements.txt
│   # 依赖文件
├── .gitignore
│   # 忽略文件
└── README.md
    # 项目说明文件
```
### 快速上手 <span style="color: #e67e22;">Quick Start</span>

#### 克隆项目 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### 安装依赖 📦
推荐使用虚拟环境管理依赖：

#### 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
## 安装依赖

```bash
pip install -r requirements.txt
```

## 添加文档 📄
将你的 PDF 文件添加到 `documents/` 文件夹下。

## 运行程序 🚀
```bash
python main.py
```

程序会自动加载 `documents/` 文件夹中的所有 PDF 文件，生成向量嵌入，并进入交互式问答模式。

## 特殊指令 <span style="color: #1abc9c;">Special Commands</span>
- 退出程序：输入 `q` 🚪
- 清除记忆：输入 `clear` 🧼

## 模块设计 <span style="color: #3498db;">Module Design</span>

### 文档加载模块 (loader/pdf_loader.py)
```
负责递归扫描指定文件夹并加载所有 PDF 文档内容。支持大文件分页加载。
核心函数：`load_documents_from_folder(folder_path)`
```
### 嵌入生成模块 (embeddings/generate_embeddings.py)
```
使用 Ollama 的嵌入模型生成向量表示，并存储在内存向量数据库中。
核心函数：`generate_embeddings(docs)`
```
### 问答模块 (qa/qa_with_context.py)
```
基于用户提问，从向量数据库中检索相关上下文，生成回答。
```
### 记忆模块（memory/memory_manager.py）
```
记录用户的提问和回答历史，支持上下文关联以及记忆清除。
核心函数：
add_to_memory(question, answer)
get_full_memory()
clear_memory()
```

## 🌟 示例使用

## 加载文档并生成回答
假设你有以下提问：
```
> 请你简单总结一下各文档的内容
```
程序会从加载的文档中检索相关上下文，并生成以下回答：
```
> 深蓝: 这段文本主要讨论了图神经网络（GNNs）在处理图形数据时遇到的挑战，特别是关于如何通过几何增强来提高其表现力。以下是几个关键点：

1. **训练过程中的问题**：图神经网络在训练过程中会面临过平滑（over-smoothing）和过度挤压（over-squashing）的问题。这些问题是由于网络深度增加导致节点表示变得无法区分或重要信息被压缩所引起的。

2. **通过重构来解决这些问题**：一种缓解方法是使用基于图形离散曲率的预处理技术，即“重连”过程。这种方法在高曲率区域移除边，在低曲率区域添加新边，以减少过平滑和过度挤压的影响。

3. **图神经网络的学习能力限制**：标准消息传递机制的GNNs不能学习到如果两幅图像拓扑不同，则它们表示不同的映射关系。这意味着GNNs可能无法学习某些基本功能，如计算图形直径或确定最大环路大小。

4. **增强表现力的方法**：为了提高图神经网络的表现能力，可以通过增加几何信息来丰富节点表示，例如使用拉普拉斯谱（Laplacian spectrum）和离散曲率。这些技术能够帮助GNNs学习更多关于图形的结构信息。       

5. **基于离散曲率的信息捕获方式**：离散曲率可以捕捉到一个节点两跳邻居内的局部结构信息，而消息传递机制只能获取一跳邻域内的信息。

综上所述，本文讨论了图神经网络如何利用几何增强技术来克服现有的局限性，并提高其在图形数据处理上的能力。这些方法为解决GNNs的过平滑和过度挤压问题提供了一种有效途径，同时也有助于增强节点表示的学习过程，使之更适合下游任务的应用需求。
```
## 对话历史记录
用户可以在多轮对话中保留上下文：
```
你：曙光万物团队的核心业务是什么？
深蓝：曙光万物团队的核心业务是推动人工智能技术在教育、医疗和工业中的应用。
```
```
你：他们的目标是什么？
深蓝：曙光万物团队致力于培养新一代的技术人才并推动技术创新。
```
用户输入 `clear` 即可清除记忆：
```
你：clear
深蓝：对话历史已清除。
```
用户输入`q`退出程序
```
你：q
(此处程序已退出，故无输出)
```
## 🛠️ 技术栈

- 编程语言：**Python >= 3.8**
- 模型：**Ollama Embeddings**, **Ollama LLM**
- 框架：**LangChain**
- 数据库：内存向量存储（可扩展为 **Pinecone**、**Weaviate** 等）

## 📖 扩展功能

- **支持其他文档格式**：
  - 目前仅支持 **PDF**，未来可扩展为支持 **.txt**、**.docx** 等格式。
- **持久化向量存储**：
  - 当前使用内存存储，推荐扩展为基于 **SQLite**、**Pinecone** 等的持久化存储。
- **集成 API**：
  - 可添加 **RESTful** 或 **gRPC** 接口，便于与前端或其他系统集成。
- **云端部署**：
  - 可部署至 **AWS**、**GCP** 或 **Azure** 构建企业级知识库。
- **多语言支持**：
  - 当前默认回答为 **中文**，支持扩展多语言问答。

## 🤝 贡献指南

欢迎贡献代码、报告 Bug 或提交功能需求！

## 📜 许可证

本项目基于 **GPL-3.0 license** 开源，欢迎自由使用和修改。

