def words_counter(book):
    return len(book.split())

def characters_counter(book):
    character_dict = {}
    for char in book:
        char_lower = char.lower()
        character_dict[char_lower] = character_dict.get(char_lower, 0) + 1
    return character_dict

def sorted_list(char_dict):
    def sort_on(dict_item):
        return list(dict_item.values())[0]

    dict_list = []
    for char in char_dict:
        dict_list.append({char: char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
