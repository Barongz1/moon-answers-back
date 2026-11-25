"""The Moon Finally Answers Back — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The line: the Moon finally answers back.
TEXT = "I have heard every wish, every howl, and every 2 AM promise to change — and I am still up here, waiting for one of you to actually do it."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
