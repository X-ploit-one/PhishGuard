from pathlib import Path
import csv
from email import policy
from email.parser import BytesParser

DATASET_DIR = Path("dataset")
HAM_DIR = DATASET_DIR / "easy_ham"
SPAM_DIR = DATASET_DIR / "spam"
OUTPUT_FILE = DATASET_DIR / "emails.csv"


def extract_email_text(file_path):
    with file_path.open("rb") as f:
        message = BytesParser(policy=policy.default).parse(f)

    subject = message.get("subject", "")
    body_parts = []

    if message.is_multipart():
        for part in message.walk():
            if (
                part.get_content_type() == "text/plain"
                and part.get_content_disposition() != "attachment"
            ):
                try:
                    body_parts.append(part.get_content())
                except Exception:
                    pass
    else:
        try:
            body_parts.append(message.get_content())
        except Exception:
            pass

    text = subject + "\n" + "\n".join(body_parts)
    return text.strip()


rows = []
errors = 0

print("Reading HAM emails...")

for file_path in HAM_DIR.iterdir():
    if file_path.is_file():
        try:
            text = extract_email_text(file_path)
            if text:
                rows.append([text, "ham"])
        except Exception:
            errors += 1

print("Reading SPAM emails...")

for file_path in SPAM_DIR.iterdir():
    if file_path.is_file():
        try:
            text = extract_email_text(file_path)
            if text:
                rows.append([text, "spam"])
        except Exception:
            errors += 1


print("Saving dataset...")

with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["email_text", "label"])
    writer.writerows(rows)

print("\nDataset preparation complete!")
print(f"Total emails: {len(rows)}")
print(f"Errors skipped: {errors}")
print(f"Saved to: {OUTPUT_FILE}")