# 🤖💡 LangOllamaQ(Deep Blue)

<div align="center">

[简体中文](README_CN.md) / [繁体中文](README_TC.md) / English / [Deutsch](README_DE.md) / [日本語](README_JP.md)

</div>

---

<span style="color: #2ecc71;" >Project Overview</span>

LangOllamaQ is a local knowledge-based Q&A system based on 🤖 <span style="color: #e74c3c;" >LangChain</span> and 📚 <span style="color: #e74c3c;" >Ollama model framework </span> construction. It is able to easily load multiple documents in a local folder, generate embedded and stored in a vector database, implement a question-and-answer function based on document context, and record conversation history to build an AI semantic search assistant for continuous interaction. 🔍 📚

<span style="color: #f1c40f;" >Features</span>

- ** Multi-document support ** : recursively scan folders and load all PDF documents. 📁
- ** Efficient vector storage ** : Use Ollama embedding model to generate text vectors and store them, supporting the most efficient content-based retrieval **. 🔍
- ** Semantic Question Answering function ** : Generate accurate and context-appropriate answers based on context. 💬
- ** Memory module ** : Record user conversation history, support dynamic query, update and clear. 💾
- ** Extensibility ** : Easy integration with other document types (e.g..txt,.docx) or persistent vector storage schemes. 🔧

> 💡 <span style="color: #f1c40f;" >** Note **</span> : This product is currently in beta and the contents of the knowledge base are provided for testing purposes only. When deploying products in real-world environments, users need to incorporate industry-specific knowledge as needed.

<span style="color: #9b59b6;" >Project Structure</span>

```plaintext
LangOllamaQ/
├── documents/
│ # Store all PDF documents
├── loader/
│   └── pdf_loader.py
│ # Scan and load documents in folders
├── embeddings/
│   └── generate_embeddings.py
│ # Generate vector embedded and stored
├── qa/
│   └── qa_with_context.py
│ # Generate responses based on context
├── memory/
│   └── memory_manager.py
│ # Record and manage user conversation history
├── main.py
│ # Main program entry
├── requirements.txt
│ # dependent file
├── .gitignore
│ # Ignore files
└── README.md
```
# Project description file

<span style="color: #e67e22;" >Quick Start</span>

#### The cloning project 🖥️
```bash
git clone https://github.com/abossss/LangOllamaQ.git
cd LangOllamaQ
```
### Installation depends on 📦
Virtual environments are recommended to manage dependencies:

#### Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
## Install dependencies

```bash
pip install -r requirements.txt
```

## Add documentation 📄
Add your PDF file to the documents/ folder.

Run the program 🚀
```bash
python main.py
```

The program will automatically load all PDF files in the 'documents/' folder, generate vector embedding, and enter the interactive question and answer mode.

<span style="color: #1abc9c;" >Special Commands</span>
- Exit the program: enter 'q' 🚪
- clear memory: Enter 'clear' 🧼

<span style="color: #3498db;" >Module Design</span>

### Document loading module (loader/pdf_loader.py)
```
Responsible for recursively scanning the specified folder and loading all PDF document contents. Supports page loading of large files.
Core function: load_documents_from_folder(folder_path)
```
embeddings/generate_embeddings.py
```
The vector representation is generated using Ollama's embedded model and stored in the in-memory vector database.
Core function: 'generate_embeddings(docs)'
```
### Q&A module (qa/qa_with_context.py)
```
Based on user questions, the relevant context is retrieved from the vector database to generate responses.
```
### memory module (memory/memory_manager.py)
```
Record the user's question and answer history, support context and memory clearing.
Core function:
add_to_memory(question, answer)
get_full_memory()
clear_memory()
```

## 🌟 example use

## Load the document and generate the answer
Suppose you have the following questions:
```
> Please briefly summarize the contents of each document
```
The program retrieves the relevant context from the loaded document and generates the following response:
```
Deep Blue: This text focuses on the challenges that graph neural networks (GNNs) encounter when working with graph data, specifically regarding how to improve their performance through geometric enhancement. Here are a few key points:

1. Problems in the training process ** : The graph neural network will face the problems of over-smoothing and over-squashing in the training process. These problems are caused by the increasing depth of the network, which causes the node representation to become indistinguishable or important information to be compressed.

2. ** Solve these problems by refactoring ** : One mitigation approach is to use a pre-processing technique based on the discrete curvature of the graph, the "reconnection" process. This method removes edges in areas of high curvature and adds new edges in areas of low curvature to reduce the effects of over-smoothing and over-squeezing.

3. ** Graph neural network learning limitations ** : The GNNs of the standard messaging mechanism cannot learn that if two images are topologically different, they represent different mapping relationships. This means that GNNs may not be able to learn certain basic functions, such as calculating the graph diameter or determining the maximum loop size.

4. ** Ways to enhance expressiveness ** : In order to improve the performance of graph neural networks, the node representation can be enriched by adding geometric information, such as using the Laplacian spectrum and discrete curvature. These techniques help GNNs learn more about the structure of graphs.

5. ** Information capture method based on discrete curvature ** : discrete curvature can capture the local structure information in the two-hop neighborhood of a node, while the message passing mechanism can only obtain information in the one-hop neighborhood.

In summary, this paper discusses how graph neural networks can use geometric augmentation techniques to overcome existing limitations and improve their ability in graph data processing. These methods provide an effective way to solve the problem of over-smoothing and over-squeezing GNNs, and also help to enhance the learning process of node representation and make it more suitable for the application requirements of downstream tasks.
```
## Conversation history
Users can retain context in multiple rounds of conversations:
```
You: What is the core business of Shuguang Everything team?
Deep Blue: The core business of the Dawning Everything team is to promote the application of artificial intelligence technology in education, healthcare and industry.
```
```
You: What are their goals?
Deep Blue: Dawn Everything team is committed to training a new generation of technical talents and promoting technological innovation.
```
The user enters' clear 'to clear the memory:
```
You: clear
Deep Blue: The conversation history has been cleared.
```
The user enters' q 'to exit the program
```
You: q
(The program has exited here, so there is no output)
```
## 🛠️ Technology stack

Programming language: **Python >= 3.8**
Model: **Ollama Embeddings**, **Ollama LLM**
- Frame: **LangChain**
- Database: Memory vector storage (expandable to **Pinecone**, **Weaviate**, etc.)

## 📖 Extended functionality

- ** Support other document formats ** :
- Currently only support **PDF**, the future can be expanded to support **.txt**, **.docx** and other formats.
- ** Persistent vector storage ** :
- Currently using memory storage, it is recommended to expand to persistent storage based on **SQLite**, **Pinecone**, etc.
- ** Integration API** :
- You can add a **RESTful** or **gRPC** interface for easy integration with front-end or other systems.
- ** Cloud Deployment ** :
- Can be deployed to **AWS**, **GCP**, or **Azure** to build an enterprise-grade knowledge base.
- ** Multi-language support ** :
- The current default answer is ** Chinese **, support for extended multi-language Q&A.

## 🤝 Contribute Guidelines

Welcome to contribute code, report bugs, or submit feature requirements!

## 📜 license

This project is open source based on **GPL-3.0 license**. You are welcome to use and modify it freely.