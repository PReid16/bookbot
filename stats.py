def get_num_words(filepath):
    i = 0
    with open(filepath) as fp:
        full_text = fp.read()
        words_list = full_text.split()
        for words in words_list:
            i += 1
    return i

def get_num_char(filepath):
    i = 1
    letters = {}
    with open(filepath) as fp:
        full_text = fp.read()
        lowercase_text = full_text.lower()
        for char in lowercase_text:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

    return letters
        
def sort_on(d):
    return d["num"]

def sorted_characters(letters):
    letters_list = []
    for letter in letters:
        if letter.isalpha():
            letter_dict = {"char": letter, "num": letters[letter]}
            letters_list.append(letter_dict)
    letters_list.sort(reverse=True, key=sort_on)
    
    return letters_list