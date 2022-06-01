from .creations import Creation
from .creation_types import CipherType
from . import ciphers


class CipherCreation(Creation):
    def __init__(self, plaintext: str):
        """
        initial_string is used to hold the original input used for the ciphers.
        cipher_types is an array of all ciphers used and their modifiers on the initial_string
        """

        super().__init__()
        self.plaintext = self._sanitize(user_input=text)
        self.cipher_types: list = []

    def caeser(self, shift: int) -> str:
        """
        Utilize Basic Caeser Cipher. Numbers and special characters are ignored.
        """

        if not self.cipher_types:
            self.creation = self.initial_string

        self.creation = ciphers.caeser(plaintext=self.creation, shift=shift)

        _ = {
            "cipher": CipherType.CAESER_CIPHER,
            "shift": shift
        }
        self.cipher_types.append(_)
        return self.creation

