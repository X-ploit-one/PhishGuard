import tarfile
from pathlib import Path

dataset_folder = Path("dataset")

files = [
    dataset_folder / "20021010_easy_ham.tar.bz2",
    dataset_folder / "20021010_spam.tar.bz2"
]

for file in files:
    print(f"\nExtracting: {file.name}")

    with tarfile.open(file, "r:bz2") as tar:
        tar.extractall(dataset_folder)

    print("Done!")

print("\nAll files extracted successfully.")