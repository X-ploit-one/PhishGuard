import pandas as pd

INPUT_FILE = "dataset/emails.csv"
OUTPUT_FILE = "dataset/clean_emails.csv"

df = pd.read_csv(INPUT_FILE)

print("Original emails:", len(df))

df = df.drop_duplicates(subset=["email_text"])

print("After removing duplicates:", len(df))

df.to_csv(OUTPUT_FILE, index=False)

print("Clean dataset saved to:", OUTPUT_FILE)