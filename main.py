import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import char_count
from stats import sort_char_count

def main(p):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {p}...")
    print("----------- Word Count ----------")
    with open(p) as f:
        txt = f.read()
        word_count = len(txt.split())
        print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_char = sort_char_count(char_count(p))
    
    for char_dict in sorted_char:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


book_path = sys.argv[1]

main(book_path)







