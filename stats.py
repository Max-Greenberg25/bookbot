from string import ascii_lowercase as alc

def count_words(book_contents):
    return len(book_contents.split())

def count_letters(book_contents):
    lowercase = book_contents.lower()
    letter_counts = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for letter in lowercase:
        if letter in alc:
            letter_counts[letter] += 1
    return letter_counts

def order_dict(char_dict):
    ordered_count = []
    for letter, count in char_dict.items():
        char_info = {
            "char": letter,
            "count": count
        }
        ordered_count.append(char_info)

    def sort_on(dict):
        return dict["count"]
    
    ordered_count.sort(reverse=True, key=sort_on)
    return ordered_count