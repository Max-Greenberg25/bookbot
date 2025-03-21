from stats import count_words

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
    return book_contents

def main():
    print(f"{count_words(get_book_text('./books/frankenstein.txt'))} words found in the document")


main()

