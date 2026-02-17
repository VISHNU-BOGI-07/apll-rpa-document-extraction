import re


# ----------------------------------
# LINE ITEMS (RAW BLOCK EXTRACTION)
# ----------------------------------
def extract_line_items(text):

    lines = text.split("\n")
    items = []
    capture = False

    for line in lines:

        if "ITEMS" in line.upper():
            capture = True
            continue

        if capture:
            if "SUMMARY" in line.upper():
                break

            if line.strip() != "":
                items.append(line.strip())

    return items


# ----------------------------------
# INVOICE EXTRACTION
# ----------------------------------
def extract_invoice(text):

    # Invoice Number
    invoice_no = re.search(
        r"(Invoice\s*No|Invoice\s*Number)[:\-]?\s*(\d+)",
        text,
        re.IGNORECASE
    )

    # Invoice Date (any date pattern)
    date_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    invoice_date = date_match.group(0) if date_match else None

    # Vendor Name
    vendor = None
    vendor_patterns = [
        r"Seller[:\-]?\s*(.*)",
        r"Vendor[:\-]?\s*(.*)"
    ]

    for p in vendor_patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            vendor = match.group(1).strip()
            break

    # Line Items
    items = extract_line_items(text)

    # Total Amount (from summary)
    total_match = re.search(r"Total\s*\$\s*([\d\s,]+)", text)
    total_amount = total_match.group(1).strip() if total_match else None

    return {
        "Vendor Name": vendor,
        "Invoice Number": invoice_no.group(2) if invoice_no else None,
        "Invoice Date": invoice_date,
        "Total Amount": total_amount,
        "Line Items": items
    }


# ----------------------------------
# PACKING LIST EXTRACTION
# ----------------------------------
def extract_packing_list(text):

    po = re.search(
        r"(PO|Purchase Order)\s*(Number|No)[:\-]?\s*(\S+)",
        text,
        re.IGNORECASE
    )

    ship_to = None
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "SHIP TO" in line.upper():
            if i + 1 < len(lines):
                ship_to = lines[i + 1].strip()
            break

    items = extract_line_items(text)

    return {
        "PO Number": po.group(3) if po else None,
        "Ship To": ship_to,
        "Line Items": items
    }
