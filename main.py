import string

def main() -> None:
    book_path: str = r"books/frankenstein.txt"
    book: str = get_book_text(book_path)
    word_count: int = count_words(book)
    print(f"word count is {word_count}")
    letter_count = count_letters(book)
    print(f"the char dict is {letter_count}")
    generate_report(book_path = book_path, word_count = word_count, chars_dict_list = letter_count)
    
def count_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)

def get_book_text(file: str) -> str:
    with open(file) as f:
        return f.read()

def count_letters(text: str) -> list[dict[str:str, str:int]]:
    lower_case_text: str = text.lower()
    letters_list: list[dict[str:str, str:int]] = []
    for letter in string.ascii_lowercase:
        num = lower_case_text.count(letter)
        letters_list.append({"char":letter, "num":num})
    return letters_list

def sort_on(dict: dict[str:str, str:int]):
    return dict["num"]

def generate_report(book_path: str, word_count: int, chars_dict_list: list[dict[str:str, str:int]], dict_key: str = "num") -> None:
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    chars_dict_list.sort(reverse=True, key = sort_on)
    for char in chars_dict_list:
        letter: str = char["char"]
        num: int = char["num"]
        print(f"The '{letter}' character was found {num} times")
    print("--- End Report ---")


if __name__ == "__main__":
    main()