import string


class CaeserCipher:
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
                result += chr((ord(char) + self.shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + self.shift - 97) % 26 + 97)
        return result

    def bruteforce(self) -> list:
        """
        Used to get a list every possible cipher for the input ciphered_text.
        """
        bf_results = []
        for i in range(1, 26):
            self.shift = i
            bf_results.append(self.encipher())
        return bf_results
