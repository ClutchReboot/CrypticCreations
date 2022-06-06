from .tools import Tools


class Rot13Cipher(Tools):
    def __init__(self, text: str):
        self.text = text

    def encipher(self) -> str:
        """
        ROT13 Cipher used on a string.
        Identical to Caeser's Cipher except shift is hard coded to 13.
        :return: Ciphered string.
        """

        result = ""
        shift = 13

        for char in self.text:
            if self.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (self.ascii_to_index(letter=char) + shift) % 26
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (self.ascii_to_index(letter=char) + shift) % 26
                result += self.index_to_ascii(index=enciphered_index)
        return result

    def decipher(self) -> str:
        """
        Since there's only one possibility with ROT13, just call original encipher method.
        """

        return self.encipher()
