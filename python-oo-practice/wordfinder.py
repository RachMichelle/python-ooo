"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """tool to find a random word from a file"""

    def __init__(self, file):
        """read file provided in arguement and call parse function"""

        file_dictionary = open(file)
        self.words = self.parse(file_dictionary)
        print("File read")
 
    def __repr__(self):
        return f"WordFinder(dictionary_file)"

    def parse(self, file_dictionary):
        """parse file into word list"""

        return [word.strip() for word in file_dictionary]

    def random(self):
        """return random word from word list"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    def parse(self, file_dictionary):
        """parse file into word list, condition to ignore lines starting with # to indicate comment"""

        return [word.strip() for word in file_dictionary if not word.startswith('#')]