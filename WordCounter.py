import re
from instrumentation_decorator import instrument

class WordCounter:
    def __init__(self, path):
        self.words = {}
        self.path = path
        self.contractions = []

    @instrument
    def count_words(self):
        self.__load()
        self.__read_words()

        sorted_words = sorted(self.words, key=lambda x: self.words[x], reverse=True)

        return {word: self.words[word] for word in sorted_words}

    @instrument
    def __load(self):
        with open('contractions.txt', 'r') as fp:
            self.contractions = [contraction.strip()
                                 for contraction in fp.read().split()]

    @instrument
    def __read_words(self):
        with open(self.path, 'r') as fp:
            words = self.__extract_words(fp.read().lower())
            for word in words:
                if word in self.words:
                    self.words[word] += 1
                else:
                    self.words[word] = 1

    @instrument
    def __extract_words(self, line):
        return [match for match in [word for word in line.split() if re.match('\w+', word)]
                if match not in self.contractions]
