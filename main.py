def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    print(book_content)


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


main()
