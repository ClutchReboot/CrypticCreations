from .creations import *
from .ciphers import *


class CipherCreation(Creation):
    def __init__(self, text: str) -> None:
        """
        initial_string is used to hold the original input used for the ciphers.
        cipher_types is an array of all ciphers used and their modifiers on the initial_string
        """

        super().__init__()
        self.text = self._sanitize(user_input=text)
        self.cipher_types: list = []

    def caeser(self, shift: int) -> str:
        """
        Utilize Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = CaeserCipher(text=self.creation, shift=shift).encipher()

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
            self.creation = self.text
        return CaeserCipher(text=self.creation).bruteforce()

    def rot13(self) -> str:
        """
        Utilize ROT13 cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = Rot13Cipher(text=self.creation).encipher()

        _ = {
            "cipher": CipherType.ROT13_CIPHER
        }
        self.cipher_types.append(_)
        return self.creation

    def rot13_bf(self) -> list:
        """
        "Bruteforce" ROT13 ciphered text. Since this cipher is so simple, there is only 1 possibility.
        :return: List of 1 string.
        """

        if not self.creation:
            self.creation = self.text
        return Rot13Cipher(text=self.creation).bruteforce()

    def affine(self, a_shift: int = 3, b_shift: int = 10) -> str:
        """
        Utilize Affine cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = AffineCipher(text=self.creation, a=a_shift, b=b_shift).encipher()

        _ = {
            "cipher": CipherType.AFFINE_CIPHER,
            "a_shift": a_shift,
            "b_shift": b_shift,
        }
        self.cipher_types.append(_)
        return self.creation
