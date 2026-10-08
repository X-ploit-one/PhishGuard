import joblib

# Load saved model and vectorizer
model = joblib.load("model/email_classifier.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Test email
email = """
URGENT! Your account has been suspended.
Click here immediately to verify your password.
"""

# Convert email into TF-IDF features
email_tfidf = vectorizer.transform([email])

# Make prediction
prediction = model.predict(email_tfidf)[0]

# Get probabilities
probabilities = model.predict_proba(email_tfidf)[0]

ham_probability = probabilities[0]
spam_probability = probabilities[1]

print("Prediction:", prediction.upper())
print(f"Ham probability: {ham_probability:.2%}")
print(f"Spam probability: {spam_probability:.2%}")