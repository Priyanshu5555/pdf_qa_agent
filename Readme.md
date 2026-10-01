# 📄 PDF Q&A RAG Agent

A **Retrieval-Augmented Generation (RAG)** based PDF Question Answering system built using Python.

This project allows users to ask questions about information contained in a PDF. The system extracts text from the document, splits it into smaller chunks, converts the chunks into embeddings, stores them in a vector database, retrieves the most relevant information, and generates an answer based on the retrieved context.

---

##   Project Workflow

```text
                PDF Document
                     │
                     ▼
              Text Extraction
                     │
                     ▼
                chunk.py
              Text Chunking
                     │
                     ▼
              embedding.py
             Generate Embeddings
                     │
                     ▼
              Vector Database
                Store Vectors
                     │
                     ▼
                query.py
             Similarity Search
                     │
                     ▼
              Relevant Chunks
                     │
                     ▼
                LLM / Answer
```

---

##   Technologies Used

* **Python**
* **PyMuPDF** – PDF text extraction
* **Embeddings** – Converts text into numerical vectors
* **ChromaDB** – Vector database for storing and searching embeddings
* **RAG (Retrieval-Augmented Generation)** – Retrieves relevant information before generating an answer

---

##   Project Structure

```text
pdf_qa_agent/
│
├── documents/
│   └── sample.pdf
│
├── main.py
├── chunk.py
├── embedding.py
├── query.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File               | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| `main.py`          | Main entry point of the project                          |
| `chunk.py`         | Extracts and divides PDF text into smaller chunks        |
| `embedding.py`     | Generates embeddings for the text chunks                 |
| `query.py`         | Performs similarity search and retrieves relevant chunks |
| `documents/`       | Contains the PDF documents used for the project          |
| `requirements.txt` | Contains required Python libraries                       |
| `README.md`        | Project documentation                                    |

---

##   Features

*   Extract text from PDF documents
*   Split large documents into smaller chunks
*   Generate embeddings for document chunks
*   Store embeddings in a vector database
*   Perform similarity-based retrieval
*   Ask questions about the uploaded document
*   Retrieve relevant document information for answering questions

---

##   Understanding RAG

**RAG stands for Retrieval-Augmented Generation.**

Instead of asking an LLM to answer a question only from its existing knowledge, RAG first retrieves relevant information from a given document and uses that information to generate the answer.

### 1. Text Extraction

The PDF is opened and its text is extracted using **PyMuPDF**.

### 2. Chunking

The extracted text is divided into smaller sections called **chunks**.

For example:

```text
Large PDF
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

Chunking makes it easier to search for specific information.

### 3. Embeddings

Each chunk is converted into a numerical representation called an **embedding**.

Similar pieces of text have similar vector representations.

```text
Text Chunk
    ↓
Embedding Model
    ↓
Vector
```

### 4. Vector Database

The generated embeddings are stored in a **vector database**.

This allows the system to efficiently search for chunks that are semantically similar to a user's question.

### 5. Query & Retrieval

When the user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Most Relevant Chunks
```

The relevant chunks are retrieved from the vector database.

### 6. Answer Generation

The retrieved information can then be used as context to generate an answer to the user's question.

```text
Question + Retrieved Context
              ↓
             LLM
              ↓
           Answer
```

---

##   Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd pdf_qa_agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##   Add a PDF

Place your PDF inside the `documents` folder.

Example:

```text
documents/
└── sample.pdf
```

You can then process the document using the project workflow.

---

##   Running the Project

Run the Python files according to the project workflow.

For example:

```bash
python main.py
```

The system processes the document and allows questions to be asked about the PDF.

Example:

```text
Question: What technologies are mentioned in the document?

Answer: Python, C++, SQL, and Java.
```

---

##   Example RAG Pipeline

Suppose the PDF contains:

```text
Python is a high-level programming language.
It is widely used in artificial intelligence and data science.
```

The system processes it as:

```text
PDF
 ↓
Extract Text
 ↓
Create Chunks
 ↓
Generate Embeddings
 ↓
Store in ChromaDB
 ↓
User asks:
"What is Python used for?"
 ↓
Similarity Search
 ↓
Retrieve relevant chunk
 ↓
Generate Answer
```

---

##   Future Improvements

* Support multiple PDF documents
* Improve chunking strategy
* Add page/source references to answers
* Improve retrieval accuracy
* Add conversational memory
* Build a web interface
* Add a chat-based UI
* Improve document preprocessing

---

##   Author

**Priyanshu Yadav**

B.Tech – Information Technology

GitHub:
https://github.com/Priyanshu5555

LinkedIn:
https://linkedin.com/in/priyanshu-yadav-5ab66a279

---

  **If you find this project useful, consider giving it a star!**
