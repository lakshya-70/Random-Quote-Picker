#47th github project --> Random Quote Picker
print('----------Random Quote Picker----------')
import random


def load_quotes(path):
    with open(path, encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
    return quotes


def main():
    print("RANDOM QUOTE PICKER")

    path = input("Quotes file path: ").strip()
    if not path:
        print("No file given.")
        return

    try:
        quotes = load_quotes(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not quotes:
        print("File has no quotes.")
        return

    print(f"\nLoaded {len(quotes)} quotes.\n")

    while True:
        print(f'"{random.choice(quotes)}"\n')
        again = input("Another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break

main()