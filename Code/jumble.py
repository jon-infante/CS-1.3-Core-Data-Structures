from hashtable import HashTable
import time


def time_it(func):
    """Time the runtime of a function that it is wrapping."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("{} took {} ms to complete".format(func.__name__, (end - start) * 1000))
        return result
    return wrapper


class Jumble(object):

    @time_it
    def __init__(self, words):
        """Initialize a new Hash Table and then clean up each line to get individual
        words. Add all the dictionary words to the hash table.
        """
        self.words = words
        self.hash = HashTable()
        lengths = []
        #Determining the lengths of the scrambled words, Speeds up the program by 5x
        for scrambled_word in words:
            if len(scrambled_word) not in lengths:
                lengths.append(len(scrambled_word))

        with open("/usr/share/dict/words", 'r') as f:
            for word in f:
                #Remove endline characters
                word = word.strip().lower()
                #Adds the word back into a hash table from the dictionary
                #Also only sets the word if it equals the length of the scrambled words
                if len(word) in lengths:
                    self.hash.set(word, word)

    def get_permutations(self, scrambled_word):
        """Get every single permutation of the scrambled word."""
        permutations = []

        if len(scrambled_word) == 1:
            return scrambled_word
        else:
            for char in scrambled_word:
                #Replacing parts of the scrambled word until we get down to 1 letter,
                #then continue to re-add strings to the character in each call
                for string in self.get_permutations(scrambled_word.replace(char, "", 1)):
                    #Checking to not repeat permutations
                    if (char + string) not in permutations:
                        permutations.append(char + string)

        return permutations

    def find_word(self, permutations):
        """Take each of the permutation of the scrambled word and look for it in the hash
        table."""
        #Look up the word in the hash table
        for perm in permutations:
            if self.hash.contains(perm):
                return self.hash.get(perm)

        return "Word not Found"

    @time_it
    def unscramble(self):
        """Unscramble each word in our list of scrambled words."""
        unscrambled = []
        for word in self.words:
            unscrambled.append(self.find_word(self.get_permutations(word)))

        return unscrambled


if __name__ == '__main__':
    scrambled_words = ['thogs', 'bannaa', 'spcieal', 'rinbaow']
    jumble = Jumble(scrambled_words)
    time_it(jumble.__init__(scrambled_words))
    # time_it(jumble.unscramble())
    # print(jumble.get_permutations("acr"))
