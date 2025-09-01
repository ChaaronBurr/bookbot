import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict
# Extracts .txt contents as a usable string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_title = sys.argv[1]
    # Gets usable text in a string.
    i = get_book_text(book_title)
    # Returns int which is the length of a list of all words.
    l = get_num_words(i)
    # Returns a dictionary with each character in the book and the number of times it appears.
    f = get_num_characters(i)
    # Takes get_num_characters and sorts key/value pairs in heirarchical order of character and count.
    j = sort_dict(f)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_title}...\n----------- Word Count ----------\nFound {l} total words\n--------- Character Count -------")
    for i in j:
        print(f"{i["character"]}: {i["count"]}")
main()