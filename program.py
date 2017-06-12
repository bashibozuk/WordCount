import sys
import os
from WordCounter import WordCounter


def main():
    if len(sys.argv) <= 1:
        print("Enter file name")
        sys.exit(0)

    path = sys.argv[1]
    if os.path.exists(path) is False:
        print("Invalid file name %s" % path)
        sys.exit(0)

    word_counter = WordCounter(path)
    print(word_counter.count_words())


if __name__ == '__main__':
    main()
