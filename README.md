# 📄 PDF Summarizer using Sentence Transformers

This project extracts and summarizes text from PDF documents using a pre-trained NLP model called `all-MiniLM-L6-v2` from Sentence Transformers. It is useful for quickly understanding the key content of long documents.

---

## 🚀 Features

- Extracts text from PDF files
- Generates meaningful summaries using semantic understanding
- Lightweight and easy to run with minimal setup
- Works offline after model download

---

## 📁 Project Structure

Round 1b/
├── input/ # Folder to place your input PDF files
├── output/ # Summarized output files will be saved here
├── generate_summary.py # Main script to extract and summarize
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## 🔧 Setup Instructions

> ✅ Recommended Python Version: **3.10** or **3.11**  
> ❌ Do **NOT** use Python 3.13 as it breaks compatibility with key libraries like NumPy and PyTorch.

### 1. Clone this repository

```bash
git clone https://github.com/your-username/pdf-summarizer.git
cd pdf-summarizer

2. Create and activate a virtual environment
bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

🛠️ How to Use
Add your PDF files into the input/ folder.

Run the following command:
python generate_summary.py
Summarized .txt files will be saved inside the output/ folder.

   
