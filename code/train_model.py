import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load training data
data = pd.read_csv('model/training_data.csv')

X = data['text']
y = data['label']

# Vectorize the text data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save the model and vectorizer
joblib.dump(model, 'model/document_classifier.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Training complete and model saved.")
