from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import joblib

# Load the trained classifier and vectorizer
classifier = joblib.load('model/document_classifier.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

def process_document(file):
    if file.filename.endswith('.pdf'):
        images = convert_from_bytes(file.read(), dpi=200)
        img = images[0]  # Process the first page of the PDF
    else:
        file.seek(0)
        img = Image.open(file)

    extracted_text = pytesseract.image_to_string(img)
    transformed_text = vectorizer.transform([extracted_text])

    document_type = classifier.predict(transformed_text)[0]
    confidence_score = max(classifier.predict_proba(transformed_text)[0])

    return {
        "extracted_info": extracted_text,
        "document_type": document_type,
        "confidence_score": round(confidence_score * 100, 2)
    }
