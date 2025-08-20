#
import sys
from stats import (
    get_sorted,
    get_stats,
    get_book_word_count,
)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path, num_words, char_stats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in char_stats:
        if char.isalpha():
            print(f"  {char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
    char_stats = get_stats(text)
    char_stats = get_sorted(char_stats)
    print_report(book_path, num_words, char_stats)

main()