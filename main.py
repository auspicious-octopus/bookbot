import sys
from stats import count_words
from stats import count_characters
from stats import sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    book_text = get_book_text(book)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict = count_characters(book_text)
    char_sorted = sort(dict)
    #print(char_sorted)
    for item in char_sorted:
        char = item["char"]
        if char.isalpha():
            total = item["num"]
            print(f"{item["char"]}: {total}")
    print("============= END ===============")

main()