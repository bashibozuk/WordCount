import re


class WordCounter:
    def __init__(self, path):
        self.words = {}
        self.path = path
        self.contractions = []

    def count_words(self):
        self.__load()
        self.__read_words()

        sorted_words = sorted(self.words, key=lambda x: self.words[x], reverse=True)

        return {word: self.words[word] for word in sorted_words}

    def __load(self):
        with open('contractions.txt', 'r') as fp:
            while True:
                line = fp.readline()
                if len(line) == 0:
                    break

                self.contractions.append(line.strip())

    def __read_words(self):
        with open(self.path, 'r') as fp:
            while True:
                line = fp.readline().lower()
                if len(line) == 0:
                    break

                words = self.__extract_words(line)
                for word in words:
                    if word in self.words:
                        self.words[word] += 1
                    else:
                        self.words[word] = 1

    def __extract_words(self, line):
        return [item for item in
                [match for match in line.split() if re.match('\w', match)]
                if item not in self.contractions]
