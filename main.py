from stats import word_counter, character_counter


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    frankenstein_book = get_book_text("/Users/stepankucera/workspace/github/draickins/bookbot/books/frankenstein.txt")
    number_of_words = word_counter(frankenstein_book)

    print(F"{number_of_words} words found in the document")
    print(character_counter(frankenstein_book))

main()
