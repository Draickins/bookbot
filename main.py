import sys
from stats import words_counter, characters_counter, sorted_list


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    number_of_words = words_counter(book)
    characters_counter_dict = characters_counter(book)

    sorted_chars = sorted_list(characters_counter_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")


    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")


main()
