from hashtable import HashTable

class Jumble(object):

    def __init__(self, words):
        """Initialize a new Hash Table and then clean up each line to get individual
        words. Add all the dictionary words to the hash table.
        """
        self.words = words
        self.hash = HashTable()
        with open("/usr/share/dict/words", 'r') as f:
            for word in f:
                #Remove endline characters
                word = word.strip().lower()
                #Adds the word back into a hash table from the dictionary
                self.hash.set(word, word)

    def get_permutations(self, scrambled_word):
        """Get every single permutation of the scrambled word."""
        permutations = []

        if len(scrambled_word) == 1:
            return scrambled_word
        else:
            for char in scrambled_word:
                for string in self.get_permutations(scrambled_word.replace(char, "")):
                    permutations.append(char + string)

        return permutations

    def find_word(self, permutations):
        """Take each of the permutation of the scrambled word and look for it in the hash
        table."""
        #Look up the word in the hash table
        for perm in permutations:
            if self.hash.contains(perm) and

                return self.hash.get(perm)

        return "Word not Found"

    def unscramble(self):
        """Unscramble each word in our list of scrambled words."""
        unscrambled = []
        for word in self.words:
            unscrambled.append(self.find_word(self.get_permutations(word)))

        return unscrambled


if __name__ == '__main__':
    scrambled_words = ['thogs', 'bannaa', 'spcieal', 'rinbaow']
    jumble = Jumble(scrambled_words)
    # print(jumble.unscramble())
