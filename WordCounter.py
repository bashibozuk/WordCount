import re
class WordCounter:
    def __init__(self, path):
        self.words = {}
        self.path = path
        self.contractions = []

    def load(self):
        fp = open('contractions.txt', 'r')
        read_from_file = True
        while read_from_file:
            line = fp.readline()
            if len(line) == 0:
                read_from_file = False
            else:
                self.contractions.append(line.strip())


        fp.close()

    def read_words(self):
        fp = open(self.path, 'r')
        while True:
            line = fp.readline().lower()
            if len(line) == 0:
                break

            words = self.extract_words(line)
            for word in words:
                if word in self.words:
                    self.words[word] += 1
                else:
                    self.words[word] = 1

        fp.close()

    def extract_words(self, line):
        for contraction in self.contractions:
            line = line.replace(contraction, '')

        line = re.sub('[\.,\-?!]', '', line)

        return line.split()

    def count_words(self):
        self.load()
        self.read_words()

        return sorted(self.words, key=lambda x: self.words[x], reverse=True)
