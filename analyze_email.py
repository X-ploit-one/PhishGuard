import joblib
from phishing_rules import analyze_email


model = joblib.load("model/email_classifier.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")


def analyze_message(email_text, subject="", sender=""):

    email_tfidf = vectorizer.transform(
        [email_text]
    )

    prediction = model.predict(
        email_tfidf
    )[0]

    probabilities = model.predict_proba(
        email_tfidf
    )[0]

    ham_probability = probabilities[0]

    spam_probability = probabilities[1]


    risk_score, risk_level, indicators = analyze_email(
        email_text + " " + subject,
        sender
    )


    ml_risk_score = round(
        spam_probability * 20
    )


    risk_score = min(
        risk_score + ml_risk_score,
        100
    )


    if risk_score >= 60:

        risk_level = "HIGH"

    elif risk_score >= 30:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"


    return {
        "prediction": prediction,
        "ham_probability": ham_probability,
        "spam_probability": spam_probability,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "indicators": indicators
    }