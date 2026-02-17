📄 Local Document Extraction System

🔍 Overview:

This project is a fully local-first Document Extraction System capable of:

Classifying Invoice and Packing List documents
Extracting key fields
Extracting line items
Generating JSON and Excel outputs
Running via Streamlit UI
No external or paid APIs are used.

🛠 Prerequisites
Please install the following before running:

1️⃣ Python

Install Python 3.10+
https://www.python.org/downloads/

2️⃣ Tesseract OCR

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

After installation, ensure the path is:

C:\Program Files\Tesseract-OCR\tesseract.exe

3️⃣ (For PDF Support Only) Poppler

Download from:
https://github.com/oschwartz10612/poppler-windows/releases

Add the Library/bin folder to your system PATH.

📦 Installation Steps

Open terminal inside project folder:

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

▶ Running the Application (UI Mode)
streamlit run app/streamlit_app.py


Then open:

http://localhost:8501


Upload Invoice or Packing List image/PDF and click Extract.

▶ Running Without UI (CLI Mode)
python app/main.py


Output files will be generated in:
output/

📂 Folder Structure:

app/ → Source code
samples/ → Sample test files
output/ → Generated JSON & Excel
design/ → Architecture & documentation
resume/ → Resume PDF

⚙ Tech Stack:

Python
Tesseract OCR
OpenCV
Pandas
Streamlit
pdf2image

🔐 Compliance:

Fully Local-first
No external APIs
No cloud services used