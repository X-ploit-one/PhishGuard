from flask import Flask, render_template, request
from analyze_email import analyze_message
import sqlite3

app = Flask(__name__)
def save_result(email_text, result):

    connection = sqlite3.connect("phishguard.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO detection_history
        (email_text, prediction, spam_probability, risk_score, risk_level)
        VALUES (?, ?, ?, ?, ?)
    """, (
        email_text,
        result["prediction"],
        result["spam_probability"],
        result["risk_score"],
        result["risk_level"]
    ))

    connection.commit()
    connection.close()

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/history")
def history():

    connection = sqlite3.connect("phishguard.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, prediction, spam_probability,
               risk_score, risk_level, timestamp
        FROM detection_history
        ORDER BY id DESC
    """)

    history_data = cursor.fetchall()

    connection.close()

    return render_template(
        "history.html",
        history=history_data
    )
@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect("phishguard.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM detection_history"
    )

    total_emails = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM detection_history WHERE risk_level = 'HIGH'"
    )

    high_risk = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM detection_history WHERE risk_level = 'MEDIUM'"
    )

    medium_risk = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM detection_history WHERE risk_level = 'LOW'"
    )

    low_risk = cursor.fetchone()[0]

    cursor.execute(
        "SELECT AVG(risk_score) FROM detection_history"
    )

    average_risk = cursor.fetchone()[0]

    connection.close()

    if average_risk is None:
        average_risk = 0
    else:
        average_risk = round(average_risk, 2)

    return render_template(
        "dashboard.html",
        total_emails=total_emails,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk,
        average_risk=average_risk
    )

@app.route("/analyze", methods=["POST"])
def analyze():

    sender = request.form.get("sender")
    recipient = request.form.get("recipient")
    subject = request.form.get("subject")
    email_text = request.form.get("email_text")

    result = analyze_message(
        email_text,
        subject,
sender
    )

    save_result(email_text, result)

    print("\n========== PHISHGUARD RESULT ==========")
    print("ML Prediction:", result["prediction"].upper())
    print(f"Spam Probability: {result['spam_probability']:.2%}")
    print("Risk Score:", result["risk_score"])
    print("Risk Level:", result["risk_level"])
    print("Indicators:", result["indicators"])

    return render_template("index.html", result=result)    
app.run(debug=True)