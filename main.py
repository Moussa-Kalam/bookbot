def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    print(book_content)

    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def count_words(text):
    return len(text.split())


main()
