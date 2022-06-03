import string
from .tools import Tools


class CaeserCipher(Tools):
    def __init__(self, text: str, shift: str = 5):
        self.text = text
        self.shift = shift

    def encipher(self) -> str:
        """
        Caeser's Cipher used on a string.
        :return: Ciphered string.
        """

        result = ""

        for char in self.text:
            # Account for spaces and special chars.
            if char not in string.ascii_letters:
                result += char
            elif char.isupper():
                enciphered_index = (self.ascii_to_index(letter=char) + self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                # result += chr((ord(char) + self.shift - 97) % 26 + 97)
                enciphered_index = (self.ascii_to_index(letter=char) + self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index)
        return result

    def bruteforce(self) -> list:
        """
        Used to get a list every possible cipher for the input ciphered_text.
        """
        bf_results = []
        for i in range(26):
            self.shift = i
            bf_results.append(self.encipher())
        return bf_results

    # TODO: Create decipher function that accepts self.creation_type value from Creations Class
