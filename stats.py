def count_words(text):
    word_list = text.split()
    total_words = 0
    for word in word_list:
        total_words += 1
    return total_words
