from ocr import extract_text
from classifier import classify
from extractor import extract_invoice, extract_packing_list
from utils import save_json, save_excel

try:
    text = extract_text(r"C:\Users\vishn\apll-rpa-document-extraction-challenge-2026-Karagatla\samples\invoices\sample1.jpg")

    doc_type = classify(text)
    print("Document Type:", doc_type)

    if doc_type == "invoice":
        data = extract_invoice(text)

    elif doc_type == "packing_list":
        data = extract_packing_list(text)

    else:
        data = {"error": "Unknown document type"}

    print(data)

    save_json(data, "../output/result.json")
    save_excel(data, "../output/result.xlsx")

    print("Extraction completed successfully")

except Exception as e:
    print("Error occurred:", e)

