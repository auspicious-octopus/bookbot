word_list = []

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    word_list = text.split()
    total_words = 0
    for word in word_list:
        total_words += 1
    return total_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()