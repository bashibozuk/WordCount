import sys
import os
from instrumentation_decorator import instrument

from WordCounter import WordCounter


@instrument
def main():
    if len(sys.argv) <= 1:
        print("Enter file name")
        sys.exit(0)

    path = sys.argv[1]
    if os.path.exists(path) is False:
        print("Invalid file name %s" % path)
        sys.exit(0)

    word_counter = WordCounter(path)
    words = word_counter.count_words()
    {print('%s:%s' % (item[0], item[1])) for item in words.items()}


if __name__ == '__main__':
    main()
