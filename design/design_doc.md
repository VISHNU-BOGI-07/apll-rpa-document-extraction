Project Title:

Local Document Extraction Service for Invoice and Packing List

Objective:
Build a local-first intelligent document extraction system capable of classifying invoices and packing lists and extracting structured data into Excel and JSON formats.

Architecture:
Input Document → Preprocessing → OCR → Classification → Extraction → Post Processing → Output

Tech Stack:
Python 3.10
Tesseract OCR
OpenCV
Pandas
OpenPyXL

Classification Logic:
Keyword-based classification using presence of words "invoice" and "packing list".

Extraction Logic:
Regex-based extraction combined with rule-based line parsing.

Exception Handling:
Try-except blocks

Missing fields return None

Logs generated

Sample Outputs:
Stored in /output folder.