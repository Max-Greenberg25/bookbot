from stats import count_words
from stats import count_letters
from stats import order_dict
import sys

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    letterCounts = count_letters(get_book_text(sys.argv[1]))
    ordered_list = order_dict(letterCounts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for i in range(0, 26):
        print(f"{ordered_list[i]["char"]}: {ordered_list[i]["count"]}")
    print("============ END ============")
main()

