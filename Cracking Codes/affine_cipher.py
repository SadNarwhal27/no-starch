"""The Affine Cipher module"""

import sys
import random
import pyperclip
import cryptomath

class AffineCipher:
    """Affine Cipher"""

    def __init__(self):
        """Initializes the Affine Cipher class"""

        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


    def _get_key_parts(self, key):
        """Breaks up a provided key into a multiplation and addition key"""

        key_a = key // len(self.SYMBOLS)
        key_b = key % len(self.SYMBOLS)
        return (key_a, key_b)
    

    def _check_keys(self, key_a, key_b, encrypt=True):
        """Checks if week keys are provided"""

        if key_a == 1 and encrypt:
            sys.exit('Cipher is weak if key A is 1. Choose a different key')
        if key_b == 0 and not encrypt:
            sys.exit('Cipher is weak if key B is 0. Choose a different key')
        # Left off on pg 191


    def encrypt_message(self, message, key):
        """Encrypts the provided message using the requested key"""