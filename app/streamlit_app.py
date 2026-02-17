import streamlit as st
import os
from ocr import extract_text
from classifier import classify
from extractor import extract_invoice, extract_packing_list
from utils import save_json, save_excel
from pdf2image import convert_from_path

st.set_page_config(page_title="Document Extraction System", layout="wide")

st.markdown(
    """
    <style>
    .title {text-align:center; font-size:36px; font-weight:bold;}
    .sub {text-align:center; font-size:18px;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>📄 Intelligent Document Extraction System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Invoice & Packing List Extractor (Local First)</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Invoice / Packing List (Image or PDF)",
    type=["jpg","png","jpeg","pdf"]
)

sample_choice = st.selectbox(
    "Or try a sample file",
    ["None","Sample Invoice","Sample Packing List"]
)

file_path = None

# SAMPLE FILES
if sample_choice == "Sample Invoice":
    file_path = "../samples/invoices/sample1.jpg"
elif sample_choice == "Sample Packing List":
    file_path = "../samples/packing_lists/sample1.jpg"

# USER UPLOAD
if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

# PROCESS
if file_path:

    if st.button("🚀 Extract Data"):

        with st.spinner("Processing document..."):

            # PDF Handling
            if file_path.endswith(".pdf"):
                pages = convert_from_path(file_path)
                img_path = "temp_page.jpg"
                pages[0].save(img_path,"JPEG")
                text = extract_text(img_path)
                os.remove(img_path)
            else:
                text = extract_text(file_path)

            doc_type = classify(text)

            if doc_type == "invoice":
                data = extract_invoice(text)
            elif doc_type == "packing_list":
                data = extract_packing_list(text)
            else:
                data = {"error":"Unknown document"}

            save_json(data,"../output/result.json")
            save_excel(data,"../output/result.xlsx")

        st.success("Extraction Completed")

        # Confidence Score
        filled = sum(v is not None for v in data.values())
        confidence = round((filled/len(data))*100,2)

        col1,col2 = st.columns(2)

        with col1:
            st.write("### Document Type")
            st.write(doc_type)
            st.write("### Confidence Score")
            st.progress(confidence/100)
            st.write(f"{confidence}%")

        with col2:
            st.write("### Extracted Data")
            st.json(data)

        with open("../output/result.json") as f:
            st.download_button("⬇ Download JSON",f,file_name="result.json")

        with open("../output/result.xlsx","rb") as f:
            st.download_button("⬇ Download Excel",f,file_name="result.xlsx")

        if uploaded_file:
            os.remove(file_path)
