import pytesseract
from preprocess import preprocess_image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):

    image = preprocess_image(image_path)
    text = pytesseract.image_to_string(image)
    return text
