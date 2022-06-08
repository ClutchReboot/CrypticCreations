from .tools import Tools


class CaeserCipher(Tools):
    def __init__(self, text: str, shift: int = 5) -> None:
        self.text = text
        self.shift = shift

    def encipher(self) -> str:
        """
        Caeser's Cipher used on a string.
        :return: Ciphered string.
        """

        result = ""

        for char in self.text:
            if self.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (self.ascii_to_index(letter=char) + self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (self.ascii_to_index(letter=char) + self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index)
        return result

    def decipher(self) -> str:
        """
        Decipher Caeser's Cipher. Shift should be the value that was used to originally encipher the text.
        :return: Ciphered string.
        """

        result = ""

        for char in self.text:
            if self.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (self.ascii_to_index(letter=char) - self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (self.ascii_to_index(letter=char) - self.shift) % 26
                result += self.index_to_ascii(index=enciphered_index)
        return result

    def bruteforce(self) -> list[str]:
        """
        Used to get a list every possible cipher for the input ciphered_text.
        """
        bf_results = []
        for i in range(26):
            self.shift = i
            bf_results.append(self.encipher())
        return bf_results
