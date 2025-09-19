def count_words(text):
    word_list = text.split()
    total_words = 0
    for word in word_list:
        total_words += 1
    return total_words

def count_characters(text):
    char_smol = text.lower()
    char_list = list(char_smol)
    char_set = set(char_list)
    char_dict = {}
    for char in char_set:
        tally = 0
        for letter in char_list:
            if char == letter:
                tally += 1
        char_dict[char] = tally
    return char_dict

def sort_on(items):
    return items["num"]

def sort(dict_in):
    dict_list = []
    for key in dict_in:
        dict_list.append({"char": key, "num": dict_in[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list