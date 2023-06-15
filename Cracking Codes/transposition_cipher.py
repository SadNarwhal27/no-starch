"""Transposition Cipher"""

import math, random, sys
import pyperclip

class TranspositionCipher:
    """Transposition Cipher"""

    def __init__(self):
        pass


    def encrypt_message(self, key, message):
        """Encryption"""

        # Each string represents a column
        cipher_text = [''] * key

        for column in range(key):
            current_index = column

            # Loops until current_index goes past message length
            while current_index < len(message):
                # Adds characters to the current column
                cipher_text[column] += message[current_index]

                # Moves the index over to the next column
                current_index += key

        cipher_text = ''.join(cipher_text)
        pyperclip.copy(cipher_text)
        return ''.join(cipher_text)


    def decrypt_message(self, key, message):
        """Decryption"""

        # Creates the grid to decrypt the provided message
        total_columns = int(math.ceil(len(message) / float(key)))
        total_rows = key
        total_shaded_boxes = (total_columns * total_rows) - len(message)

        plain_text = [''] * total_columns

        column, row = 0, 0
        for symbol in message:
            plain_text[column] += symbol
            column += 1

            # Moves to the next row once the end of the row is reached
            if (column == total_columns) or (column == total_columns - 1
                                             and row >= total_rows - total_shaded_boxes):
                column = 0
                row += 1

        plain_text = ''.join(plain_text)
        pyperclip.copy(plain_text)
        return plain_text
    

    def test_transposition(self):
        """Automated testing for the transposition module"""

        random.seed(42)

        for i in range(20):
            # Generate a random message with a random length
            message = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40))
            random.shuffle(message)
            message = ''.join(message)
            print(f"Test #{i+1}: {message[:50]}...")

            for key in range(1, int(len(message)/2)):
                encrypted = TranspositionCipher().encrypt_message(key, message)
                decrypted = TranspositionCipher().decrypt_message(key, encrypted)
                if message != decrypted:
                    print(f'Mismatch with key {key} and message {message}')
                    print(f'Decrypted as: {decrypted}')
                    sys.exit()

        print('Transposition cipher test passed.')
