from hashtable import HashTable

class Jumble(object):

    def __init__(self, words):
        """Initialize a new Hash Table and then clean up each line to get individual
        words. We then sort the words in alphabetical order and turn that sorted word
        into the key, with the original word as the value.
        """
        self.words = words
        self.hash = HashTable()
        with open("/usr/share/dict/words", 'r') as f:
            for word in f:
                #Remove endline characters
                word = word.strip().lower()
                #Sort the word alphabetically and putting it into a string instead of a list
                sorted_word = ''.join(sorted(word))
                #Adds the word back into a hash table from the dictionary
                self.hash.set(sorted_word, word)

    def find_word(self, scrambled_word):
        """Turn the scrambled word into sorted order, and look up for a match
        in the hash table."""
        sorted_word = ''.join(sorted(scrambled_word))

        if self.hash.contains(sorted_word):
            return self.hash.get(sorted_word)

        return "Word not Found"

    def unscramble(self):
        """Unscramble each word in our list of scrambled words."""
        unscrambled = []
        for word in self.words:
            unscrambled.append(self.find_word(word))

        return unscrambled


if __name__ == '__main__':
    scrambled_words = ['thogs', 'bannaa', 'spcieal', 'rinbaow']
    jumble = Jumble(scrambled_words)
    print(jumble.unscramble())
