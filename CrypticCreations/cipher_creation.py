from .creations import *
from .ciphers import *


class CipherCreation(Creation):
    def __init__(self, text: str) -> None:
        """
        initial_string is used to hold the original input used for the ciphers.
        cipher_types is an array of all ciphers used and their modifiers on the initial_string
        """

        super().__init__()
        self.text: str = self._sanitize(user_input=text)
        self.cipher_types: list[dict] = []

    def caeser(self, shift: int) -> str:
        """
        Utilize Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = CaeserCipher(text=self.creation, shift=shift).encipher()

        _ = {
            "cipher": CipherType.CAESER.value,
            "shift": shift
        }
        self.cipher_types.append(_)
        return self.creation

    def caeser_decipher(self, shift: int) -> str:
        """
        Decipher Basic Caeser. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = CaeserCipher(text=self.creation, shift=shift).decipher()

        _ = {
            "cipher": CipherType.CAESER.value,
            "shift": shift
        }
        self.cipher_types.remove(_)
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
            "cipher": CipherType.ROT13.value
        }
        self.cipher_types.append(_)
        return self.creation

    def rot13_decipher(self) -> str:
        """
        Decipher ROT13. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = Rot13Cipher(text=self.creation).decipher()

        _ = {
            "cipher": CipherType.ROT13.value
        }
        self.cipher_types.remove(_)
        return self.creation

    def rot13_bf(self) -> str:
        """
        "Bruteforce" ROT13 ciphered text. Since this cipher is so simple, there is only 1 possibility.
        :return: List of 1 string.
        """

        if not self.creation:
            self.creation = self.text
        return Rot13Cipher(text=self.creation).decipher()

    def affine(self, a_shift: int = 3, b_shift: int = 10) -> str:
        """
        Utilize Affine cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = AffineCipher(text=self.creation, a=a_shift, b=b_shift).encipher()

        _ = {
            "cipher": CipherType.AFFINE.value,
            "a_shift": a_shift,
            "b_shift": b_shift,
        }
        self.cipher_types.append(_)
        return self.creation

    def affine_decipher(self, a_shift: int = 3, b_shift: int = 10) -> str:
        """
        Decipher Affine. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.text

        self.creation = AffineCipher(text=self.creation, a=a_shift, b=b_shift).decipher()

        _ = {
            "cipher": CipherType.AFFINE.value,
            "a_shift": a_shift,
            "b_shift": b_shift,
        }
        self.cipher_types.remove(_)
        return self.creation

    def decipher(self) -> str:
        """
        Cycle through all ciphers in cipher_types and attempt to decipher them if a method exists.
        :return: deciphered text.
        """

        cipher_types_copy = self.cipher_types.copy()
        cipher_types_copy.reverse()
        for cipher_object in cipher_types_copy:
            method_args = cipher_object.copy()
            decipher_method = f"{method_args.pop('cipher')}_decipher"
            if hasattr(self, decipher_method):
                getattr(self, decipher_method)(**method_args)
                print(f"{self.creation=}")
        return self.creation
