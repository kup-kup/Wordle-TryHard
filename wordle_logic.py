#reading possible_words.txt line by line in the folder and put it in a list
possible_word = open("possible_words.txt", "r")
possible_word_list = possible_word.read().upper().split('\n')

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

def mass_filter_renew(items, poss_list):
    items_gray = [item for item in items if item.color == 'gray' and item.char.get()]
    items_yellow = [item for item in items if item.color == 'yellow' and item.char.get()]
    items_green = [item for item in items if item.color == 'green' and item.char.get()]

    ls = set()

    for letter in items_green:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        for word in poss_list[:]:
            if char not in word:
                poss_list.remove(word)
            elif char != word[index]:
                poss_list.remove(word)
            ls.add(char)

    for letter in items_yellow:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        for word in poss_list[:]:
            if char not in word:
                poss_list.remove(word)
            elif char == word[index]:
                poss_list.remove(word)
            ls.add(char)

    for letter in items_gray:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        if char not in ls:
            for word in poss_list[:]:
                if char in word:
                    poss_list.remove(word)

    return poss_list

def mass_filter_count(items, poss_list):
    items_gray = [item for item in items if item.color == 'gray' and item.char.get()]
    items_yellow = [item for item in items if item.color == 'yellow' and item.char.get()]
    items_green = [item for item in items if item.color == 'green' and item.char.get()]

    ls = set()
    char_count = dict()

    for letter in items_green:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        if char in ls:
            if char not in char_count.keys():
                char_count.update({char : 2})
            else:
                char_count[char] += 1
        ls.add(char)

        for word in poss_list[:]:
            if char not in word:
                poss_list.remove(word)
            elif char != word[index]:
                poss_list.remove(word)


    for letter in items_yellow:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        if char in ls:
            if char not in char_count.keys():
                char_count.update({char : 2})
            else:
                char_count[char] += 1
        ls.add(char)

        for word in poss_list[:]:
            if char not in word:
                poss_list.remove(word)
            elif char == word[index]:
                poss_list.remove(word)


    for letter in items_gray:
        char = letter.char.get()
        color = letter.color
        index = letter.index
        if char not in ls:
            for word in poss_list[:]:
                if char in word:
                    poss_list.remove(word)

    #print(char_count)

    for char in char_count:
        count = char_count[char]
        for word in poss_list[:]:
            if word.count(char) < count:
                poss_list.remove(word)
                #print(f'{word} removed: {word.count(char)} < {count}')

    return poss_list

def filter_by_row(items, poss_list):
    if len(items) != 25:
        raise ValueError('Items length not 25')

    row1 = mass_filter_count(items[:5], poss_list)
    row2 = mass_filter_count(items[5:10], row1)
    row3 = mass_filter_count(items[10:15], row2)
    row4 = mass_filter_count(items[15:20], row3)
    row5 = mass_filter_count(items[20:25], row4)

    return row5

def mass_filter_renew_test(items, poss_list):
    items_gray = [item for item in items if item.color == 'gray' and item.char.get()]
    for item in items_gray:
        print(item)
