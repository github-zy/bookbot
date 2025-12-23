import sys
from stats import count_words, count_characters, get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path) 
    num_words = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_list = get_sorted_list(char_dict)
    print_report(num_words, sorted_list, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(num_words, sorted_list, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()