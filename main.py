from stats import word_counter, character_counter, sorted_list


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    frankenstein_book = get_book_text("/Users/stepankucera/workspace/github/draickins/bookbot/books/frankenstein.txt")
    number_of_words = word_counter(frankenstein_book)
    character_counter_dict = character_counter(frankenstein_book)

    sorted_chars = sorted_list(character_counter_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")


    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")


main()
