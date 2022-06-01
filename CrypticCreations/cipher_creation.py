from .creations import Creation
from .creation_types import CipherType
from .ciphers import *


class CipherCreation(Creation):
    def __init__(self, plaintext: str):
        """
        initial_string is used to hold the original input used for the ciphers.
        cipher_types is an array of all ciphers used and their modifiers on the initial_string
        """

        super().__init__()
        self.plaintext = self._sanitize(user_input=plaintext)
        self.cipher_types: list = []

    def caeser(self, shift: int) -> str:
        """
        Utilize Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.plaintext

        self.creation = Caeser().encode(plaintext=self.creation, shift=shift)

        _ = {
            "cipher": CipherType.CAESER_CIPHER,
            "shift": shift
        }
        self.cipher_types.append(_)
        return self.creation

    def caeser_bf(self) -> list:
        """
        Bruteforce all possible combinations of a string using Caeser's Cipher.
        :return: List of Caeser's Cipher strings.
        """
        if not self.creation:
            self.creation = self.plaintext
        return Caeser().bruteforce(ciphered_text=self.creation)

    def rot13(self) -> str:
        """
        Utilize ROT13 cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.plaintext

        self.creation = ciphers.rot13(plaintext=self.creation)

        _ = {
            "cipher": CipherType.ROT13_CIPHER
        }
        self.cipher_types.append(_)
        return self.creation
