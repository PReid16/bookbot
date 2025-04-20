import sys
from stats import get_num_words, get_num_char, sorted_characters

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        num_words = get_num_words(book)
        print(f"Found {num_words} total words")
        chars = get_num_char(book)
        sorted_chars = sorted_characters(chars)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")

main()