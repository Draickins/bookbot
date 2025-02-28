def word_counter(book):
    words = book.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

