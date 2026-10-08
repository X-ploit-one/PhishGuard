import joblib
from pathlib import Path
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load cleaned dataset
df = pd.read_csv("dataset/clean_emails.csv")

# Input and output
X = df["email_text"]
y = df["label"]

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Total emails:", len(df))
print("Training emails:", len(X_train))
print("Testing emails:", len(X_test))

# Convert email text into TF-IDF features
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF conversion complete!")
print("Training matrix shape:", X_train_tfidf.shape)
print("Testing matrix shape:", X_test_tfidf.shape)

# Create the machine learning model
model = LogisticRegression(max_iter=1000)

# Train the model
print("\nTraining Logistic Regression model...")
model.fit(X_train_tfidf, y_train)

print("Model training complete!")

# Make predictions on test emails
predictions = model.predict(X_test_tfidf)

print("\nFirst 10 predictions:")
print(predictions[:10])
# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
# Create model folder if it doesn't exist
Path("model").mkdir(exist_ok=True)

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

# Save the trained model
joblib.dump(model, "model/email_classifier.pkl")

print("\nModel and vectorizer saved successfully!")