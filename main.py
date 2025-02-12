from collections import Counter
from collections.abc import Callable
from pathlib import Path
from typing import Final

REL_PATHS_BOOKS: Final[Path] = Path("./books/")
BOOK_TITLE: Final[str] = "Frankenstein"


def read_book_contents(title: str) -> str:
    title = title.lower()
    p_book = (REL_PATHS_BOOKS / title).with_suffix(".txt")
    assert p_book.exists(), f"book name {title} not found"

    with open(p_book, "r", encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents


def count_words(content: str) -> int:
    words = content.split()

    return len(words)


def count_characters(content: str) -> dict[str, int]:
    lowered = content.lower()
    return Counter(lowered)


def count_chars_intended(contents: str) -> dict[str, int]:
    contents = contents.lower()
    char_count: dict[str, int] = {}

    for char in contents:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count


def print_sorted_char_count(counts: dict[str, int]) -> None:
    filtered = [{"char": k, "count": v} for k, v in counts.items() if k.isalpha()]

    def sort_on(sort_key: str) -> Callable[[], int]:
        return lambda x: x[sort_key]

    filtered.sort(reverse=True, key=sort_on(sort_key="count"))

    for entry in filtered:
        print(f"The '{entry['char']}' character was found {entry['count']} times")


def print_report(contents: str) -> None:
    print("--- Begin report of books/frankenstein.txt ---")

    word_count = count_words(contents)
    print(f"{word_count} words found in the document\n")
    char_count = count_characters(contents)
    print_sorted_char_count(char_count)

    print("--- End report ---")


def main() -> None:
    contents = read_book_contents(title=BOOK_TITLE)

    # num_words_contained = count_words(contents)
    # num_chars = count_characters(contents)
    # num_chars_2 = count_chars_intended(contents)
    # print_sorted_char_count(num_chars_2)
    # print(num_chars_2)
    print_report(contents)


if __name__ == "__main__":
    main()
