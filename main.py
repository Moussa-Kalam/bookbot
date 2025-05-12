import sys

from stats import count_words, count_chars, get_char_stats_sorted


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    num_chars = count_chars(book_content)
    sorted_chars_stats_list = get_char_stats_sorted(num_chars)
    print_report(book_path, num_words, sorted_chars_stats_list)


def print_report(book_path, num_words, chars_stats_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing the book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in chars_stats_sorted:
        print(f"{entry['char']}: {entry["num"]}")
    print("============= END ===============")





def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


main()
