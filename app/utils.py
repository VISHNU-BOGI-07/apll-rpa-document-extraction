import json
import pandas as pd

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def save_excel(data, path):

    header_data = {
        "Vendor Name": data.get("Vendor Name"),
        "Invoice Number": data.get("Invoice Number"),
        "Invoice Date": data.get("Invoice Date")
    }

    header_df = pd.DataFrame([header_data])
    items_df = pd.DataFrame(data.get("Line Items"))

    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        header_df.to_excel(writer, index=False, sheet_name="Invoice_Details")
        items_df.to_excel(writer, index=False, sheet_name="Line_Items")
