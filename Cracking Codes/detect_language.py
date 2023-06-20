"""Detecting English"""

class DetectLanguage:
    """A way to detect English words within text"""

    def __init__(self, dictionary_file_name):
        """Initializes the class and constants"""

        UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + (' \t\n')
        self.WORDS = self._load_dictionary(dictionary_file_name)


    def _load_dictionary(self, dictionary_file_name):
        """Takes a dictionary txt file and turns it into a searchable dict"""

        dictionary_file = open(dictionary_file_name)
        words = {word: None for word in dictionary_file.read().split('\n')}
        dictionary_file.close()
        return words # Dictionaries are faster to search through than lists


    def _remove_non_letters(self, message):
        """Removes punctuation and other non-letters from message"""

        letters_only = []
        for symbol in message:
            if symbol in self.LETTERS_AND_SPACE:
                letters_only.append(symbol)
        return ''.join(letters_only)


    def _get_word_count(self, message):
        """Gets the ratio of real words to nonsense in message"""

        message = self._remove_non_letters(message.upper())
        possible_words = message.split()

        if possible_words == []:
            return 0.0 # No words at all

        # Counts total words in message that are in dictionary
        matches = 0
        for word in possible_words:
            if word in self.WORDS:
                matches += 1 

        return float(matches) / len(possible_words)


    def is_coherent(self, message, word_perc=50, letter_perc=85):
        """Checks if message is actually coherent and not random nonsense"""

        words_match = self._get_word_count(message) * 100 >= word_perc
        
        num_letters = len(self._remove_non_letters(message))
        message_letter_perc = (float(num_letters) / len(message)) * 100
        letters_match = message_letter_perc >= letter_perc

        return words_match and letters_match