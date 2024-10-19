import joblib

class DocumentClassifier:
    def __init__(self):
        self.model = joblib.load('model/document_classifier.pkl')
        self.vectorizer = joblib.load('model/vectorizer.pkl')

    def predict(self, text_list):
        transformed_text = self.vectorizer.transform(text_list)
        return self.model.predict(transformed_text)
