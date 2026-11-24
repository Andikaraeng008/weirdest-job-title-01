import os

TEXT = "Grief Counsellor for Retired Office Printers"

# Kit gate: /output/entry.txt must be UTF-8 text of 1 to 60 characters,
# not only white space.
assert 1 <= len(TEXT) <= 60 and TEXT.strip(), "gate violation"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
