# Learnwise-ai
# 🎓 Learwise AI (v1.0 — Open-Source RAG)

An open-source, zero-API-key **Retrieval-Augmented Generation (RAG) AI Tutor** built in GitHub Codespaces. Learwise AI helps students understand B.Tech subjects through personalized explanations using four adaptive teaching styles.

## 🌟 Key Features

- **Zero API Keys:** Uses open-source AI models without requiring paid API access.
- **Smart Knowledge Retrieval:** Retrieves relevant information from subject notes using RAG.
- **Adaptive Learning:** Explains concepts in four different teaching styles.
- **Multi-Subject Support:** Designed to support different B.Tech subjects.
- **Interactive Learning:** Allows students to ask questions and receive context-based answers.
- **Open Source:** Built using freely available open-source technologies.

## 🏗️ v1.0 Architecture

- **Project Name:** Learwise AI
- **Subject Knowledge Base:** `data/subject_notes.md`
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` (384-dimensional vectors)
- **Vector Database:** ChromaDB using Cosine Similarity
- **Open-Source LLM:** `Qwen/Qwen2.5-0.5B-Instruct` (CPU-optimized)
- **Frontend:** Streamlit
- **Development Environment:** GitHub Codespaces
- **Retrieval Method:** Retrieval-Augmented Generation (RAG)

## 🧠 Four Adaptive Learning Styles

1. **ELI10 Analogy:** Explains difficult concepts in very simple language using everyday examples and analogies.
2. **Exam Topper:** Provides structured, exam-oriented answers with important definitions, key points, and examples.
3. **Socratic Professor:** Helps students learn through questions, hints, and step-by-step reasoning.
4. **Practical Engineer:** Explains concepts through real-world applications, practical examples, and technical use cases.

## ⚙️ How RAG Works

1. **Input:** The student asks a question about a subject.
2. **Embedding:** The question is converted into a numerical vector.
3. **Retrieval:** ChromaDB searches for relevant information from the subject knowledge base.
4. **Generation:** The retrieved information is provided to the open-source LLM as context.
5. **Adaptive Response:** The AI generates an answer according to the selected learning style.

## 🚀 How to Run in GitHub Codespaces

### Step 1: Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Learwise-ai
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv .venv
```

### Step 3: Activate the Environment

```bash
source .venv/bin/activate
```

### Step 4: Install CPU-Compatible PyTorch

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Step 5: Install Project Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Launch the Application

```bash
streamlit run app.py
```

Open the forwarded Streamlit port in GitHub Codespaces to access Learwise AI.

## 📁 Project Structure

```text
Learwise-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── subject_notes.md
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | User interface |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| Qwen 2.5 | Answer generation |
| PyTorch | Model execution |
| GitHub Codespaces | Development environment |

## 🎯 Project Objective

The main objective of Learwise AI is to make technical education easier, more interactive, and accessible to every student. Instead of providing the same explanation to everyone, it offers different teaching approaches according to individual learning preferences.

## 🔮 Future Enhancements

- Support for PDF and DOCX study materials.
- Multiple B.Tech subject knowledge bases.
- Quiz generation and practice tests.
- Automatic notes summarization.
- Student progress tracking.
- Multilingual explanations.
- Improved response accuracy and retrieval performance.

## 📜 License

This project is intended for educational and open-source development. A suitable open-source license can be added to the repository.

---

**Learwise AI — Learn Smarter, Understand Better, Build Your Future! 🎓**
