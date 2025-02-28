from test.test_configparser import SortedDict
def word_counter(book):
    words = book.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def character_counter(book):
    character_dict = {}
    for char in book:
        character_dict[char.lower()] = character_dict.get(char.lower(), 0) + 1
    return character_dict

def sorted_list(char_dict):
    def sort_on(dict_item):
        return list(dict_item.values())[0]

    dict_list = []
    for char in char_dict:
        dict_list.append({char: char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
