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
