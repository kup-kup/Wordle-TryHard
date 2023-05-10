#reading possible_words.txt line by line in the folder and put it in a list
possible_word = open("possible_words.txt", "r")
possible_word_list = possible_word.read().upper().split('\n')

import re

def mass_filter(items, poss_list):
    for letter in items:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        if char:
            if color == 'gray':
                for word in poss_list[:]:
                    if char in word:
                        poss_list.remove(word)
            elif color == 'yellow':
                for word in poss_list[:]:
                    if char not in word:
                        poss_list.remove(word)
                    elif char == word[index]:
                        poss_list.remove(word)
            elif color == 'green':
                for word in poss_list[:]:
                    if char not in word:
                        poss_list.remove(word)
                    elif char != word[index]:
                        poss_list.remove(word)

    return poss_list
