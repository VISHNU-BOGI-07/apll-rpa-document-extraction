def classify(text):
    text = text.lower()

    if "invoice" in text:
        return "invoice"
    elif "packing list" in text:
        return "packing_list"
    else:
        return "unknown"
