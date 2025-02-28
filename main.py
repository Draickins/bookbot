def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_counter(book):
    words = book.split()
    counter = 0
    for word in words:
        counter += 1
    return counter


def main():
    frankenstein_book = get_book_text("/Users/stepankucera/workspace/github/draickins/bookbot/books/frankenstein.txt")
    number_of_words = word_counter(frankenstein_book)

    print(F"{number_of_words} words found in the document")


main()
