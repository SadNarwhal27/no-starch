"""Transposition Cipher"""

import math
import random
import sys
import time
import os
import pyperclip
from detect_language import DetectLanguage

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


    def file_cipher(self, input_file, output_file, key, encrypt=True):
        """Encrypts and decrypts text files"""

        # Quits the program if file does not exist
        if not os.path.exists(input_file):
            print(f"The file {input_file} does not exist. Quitting...")
            sys.exit()

        # Offers users a chance to quit if output file already exists
        if os.path.exists(output_file):
            print(f"This will overwrite the file {output_file}. (C)ontinue or (Q)uit?")
            response = input('> ')
            if not response.lower().startswith('c'):
                sys.exit()

        # Reads in file for crypting
        file_obj = open(input_file)
        content = file_obj.read()
        file_obj.close()

        print('Encrypting...' if encrypt else 'Decrypting...')

        # Measures time elapsed while crypting
        start_time = time.time()
        if encrypt:
            translated = self.encrypt_message(key, content)
        else:
            translated = self.decrypt_message(key, content)
        total_time = round(time.time() - start_time, 2)
        print(f'File ready. Time elapsed: {total_time}')

        # Writes to output file
        output_file_obj = open(output_file, 'w')
        output_file_obj.write(translated)
        output_file_obj.close()

        print(f"# of characters changed: {len(content)}")


    def hack_transposition(self, message):
        """Brute-force solve transposition ciphers"""

        print('Hacking...')
        detector = DetectLanguage('Cracking Codes/dictionary.txt')

        for key in range(1, len(message)):
            decrypted_text = self.decrypt_message(key, message)

            if detector.is_coherent(decrypted_text):
                print(f"\nPossible encryption hack:\nKey #{key}: {decrypted_text[:100]}\n"
                      "(C)ontinue?")
                response = input('> ').strip().upper()

                if response.startswith('C'):
                    pyperclip.copy(decrypted_text)
                    print(f"Message copied to clipboard:\n\n{decrypted_text}")
                    return decrypted_text

        print('Decryption failed.')
        return None
