import re


URGENCY_KEYWORDS = [
    "urgent",
    "immediately",
    "act now",
    "as soon as possible",
    "within 24 hours",
    "verify now",
    "action required"
]


CREDENTIAL_KEYWORDS = [
    "password",
    "username",
    "login",
    "verify your account",
    "confirm your identity",
    "security code",
    "otp"
]


FINANCIAL_KEYWORDS = [
    "bank",
    "credit card",
    "debit card",
    "payment",
    "transaction",
    "refund",
    "invoice"
]


ACCOUNT_THREAT_KEYWORDS = [
    "account suspended",
    "account has been suspended",
    "account blocked",
    "account has been blocked",
    "account locked",
    "account has been locked",
    "account will be closed",
    "suspicious activity",
    "unauthorized access"
]


SUSPICIOUS_SENDER_PATTERNS = [
    "paypa1",
    "micros0ft",
    "amaz0n",
    "secure-login",
    "account-verify",
    "verify-account",
    "security-alert"
]


def check_keywords(text, keywords):

    text = text.lower()

    found = []

    for keyword in keywords:

        if keyword in text:

            found.append(keyword)

    return found


def detect_urls(text):

    pattern = r"https?://\S+|www\.\S+"

    return re.findall(pattern, text, re.IGNORECASE)


def check_suspicious_urls(urls):

    suspicious_urls = []

    for url in urls:

        if re.search(
            r"https?://\d{1,3}(\.\d{1,3}){3}",
            url
        ):

            suspicious_urls.append(
                f"IP address URL: {url}"
            )

        shorteners = [
            "bit.ly",
            "tinyurl.com",
            "t.co",
            "goo.gl",
            "is.gd",
            "cutt.ly"
        ]

        if any(
            shortener in url.lower()
            for shortener in shorteners
        ):

            suspicious_urls.append(
                f"URL shortener detected: {url}"
            )

        if url.lower().startswith("http://"):

            suspicious_urls.append(
                f"Non-HTTPS URL: {url}"
            )

    return suspicious_urls


def check_sender(sender):

    sender = sender.lower().strip()

    suspicious = []

    for pattern in SUSPICIOUS_SENDER_PATTERNS:

        if pattern in sender:

            suspicious.append(pattern)

    return suspicious


def analyze_email(email_text, sender=""):

    risk_score = 0

    indicators = []


    if sender:

        suspicious_sender = check_sender(sender)

        if suspicious_sender:

            risk_score += 25

            indicators.append(
                f"Suspicious sender: {sender}"
            )


    urgency = check_keywords(
        email_text,
        URGENCY_KEYWORDS
    )

    if urgency:

        risk_score += 15

        indicators.append(
            f"Urgency detected: {', '.join(urgency)}"
        )


    credentials = check_keywords(
        email_text,
        CREDENTIAL_KEYWORDS
    )

    if credentials:

        if len(credentials) == 1:

            risk_score += 10

        else:

            risk_score += 30

        indicators.append(
            f"Credential-related language: {', '.join(credentials)}"
        )


    financial = check_keywords(
        email_text,
        FINANCIAL_KEYWORDS
    )

    if financial:

        risk_score += 25

        indicators.append(
            f"Financial language: {', '.join(financial)}"
        )


    account_threats = check_keywords(
        email_text,
        ACCOUNT_THREAT_KEYWORDS
    )

    if account_threats:

        risk_score += 20

        indicators.append(
            f"Account threat detected: {', '.join(account_threats)}"
        )


    urls = detect_urls(email_text)

    if urls:

        indicators.append(
            f"URL detected: {len(urls)} link(s)"
        )

        suspicious_urls = check_suspicious_urls(urls)

        if suspicious_urls:

            risk_score += 25

            for suspicious_url in suspicious_urls:

                indicators.append(
                    f"Suspicious URL: {suspicious_url}"
                )


    risk_score = min(
        risk_score,
        100
    )


    if risk_score >= 60:

        risk_level = "HIGH"

    elif risk_score >= 30:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"


    return risk_score, risk_level, indicators