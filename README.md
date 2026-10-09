# 🛡️ PhishGuard — Phishing Email Detection System

PhishGuard is a machine learning-based web application that helps identify potentially suspicious and phishing emails. It analyzes email text using a trained classification model and rule-based checks to highlight possible security risks.

## 🚀 Features

* **Email Classification:** Classifies email messages as Ham (legitimate) or Spam.
* **Machine Learning:** Uses TF-IDF for text feature extraction and Logistic Regression for classification.
* **Rule-Based Analysis:** Detects suspicious indicators such as urgent language, credential requests, and account threats.
* **Risk Assessment:** Generates a risk score to help users identify potentially dangerous emails.
* **Web Interface:** Provides a simple interface for submitting and analyzing email content.

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* HTML and CSS
* Enron email dataset

## ⚙️ How It Works

1. The user enters an email message into the web application.
2. The application preprocesses the email text.
3. The trained machine learning model classifies the message.
4. Rule-based checks look for suspicious patterns.
5. The application displays the classification and risk assessment.

## 📂 Project Components

* **Dataset:** Email samples used for training and evaluation.
* **Model:** Trained Logistic Regression email classifier.
* **Vectorizer:** TF-IDF model used to transform email text into numerical features.
* **Flask Application:** Handles email submissions and analysis.
* **Web Interface:** Allows users to interact with the system.

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd PhishGuard
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

Run the Python file that starts your Flask application. For example, if your entry-point file is `app.py`:

```bash
python app.py
```

Open the local URL shown in the terminal in your web browser.

## 🎯 Project Objective

The objective of PhishGuard is to demonstrate how machine learning and rule-based analysis can support phishing email detection and cybersecurity awareness.

## 🔮 Future Improvements

* Improve detection of phishing URLs and malicious links.
* Reduce false negatives for phishing emails.
* Add email header analysis.
* Improve the user interface and risk reporting.
* Evaluate the model on additional unseen email samples.

## ⚠️ Disclaimer

PhishGuard is an educational cybersecurity project. Its predictions are not guaranteed to be correct. Always verify suspicious emails independently and do not rely solely on this tool for security decisions.

## 👩‍💻 Project Contributors

* Sonal Yadav
* Sneha Kansara

---

**If you find this project useful, consider giving the repository a ⭐ on GitHub!**
