import string

from .creations import Creation
from .creation_types import CipherType


class CipherCreation(Creation):
    def __init__(self, text: str):
        """
        initial_string is used to hold the original input used for the ciphers.
        cipher_types is an array of all ciphers used and their modifiers on the initial_string
        """

        super().__init__()
        self.initial_string = self._sanitize(user_input=text)
        self.cipher_types: list = []

    def basic(self, shift: int) -> str:
        """
        Utilize Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.initial_string

        self.creation = self._create_basic(shift=shift)
        _ = {
            "cipher": CipherType.BASIC_CIPHER,
            "shift": shift
        }
        self.cipher_types.append(_)
        return self.creation

    def _create_basic(self, shift: int) -> str:
        """
        Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        result = ""
        for char in self.creation:
            # Account for spaces and special chars.
            if char not in string.ascii_letters:
                result += char
            elif char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result
