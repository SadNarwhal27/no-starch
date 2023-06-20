"""Contains the basic Caesar Cipher and brute-force solver"""

import pyperclip
from detect_language import DetectLanguage

class CaesarCipher:
    """Uses the Caesar Cipher to make 1 to 1 translations"""

    def __init__(self):
        """Initializes the cipher with message, key, and encryption mode"""

        self.SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst"
        self.SYMBOLS += "uvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'"


    def translate(self, message, key=0, encrypt=True):
        """Encrypts or decrypts a message"""

        translated_message = ''

        for symbol in message:
            if symbol in self.SYMBOLS:
                symbol_index = self.SYMBOLS.find(symbol)

                # Gets the translated index within SYMBOLS
                translated_index = symbol_index + key if encrypt else symbol_index - key

                # Handles wraparound if necessary
                if translated_index >= len(self.SYMBOLS):
                    translated_index -= len(self.SYMBOLS)
                elif translated_index < 0:
                    translated_index += len(self.SYMBOLS)

                translated_message += self.SYMBOLS[translated_index]
            else:
                translated_message += symbol

        pyperclip.copy(translated_message)
        return translated_message


    def hack_caesar(self, message):
        """Brute-force solve caesar ciphers"""

        detector = DetectLanguage('Cracking Codes/dictionary.txt')
        for key in range(len(self.SYMBOLS)):
            temp_message = self.translate(message, key=key, encrypt=False)
            if detector.is_coherent(temp_message):
                return f"Key #{key}: {temp_message}"
