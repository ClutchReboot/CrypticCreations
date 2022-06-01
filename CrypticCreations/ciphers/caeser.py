import string


class Caeser:

    @staticmethod
    def encode(plaintext: str, shift: int) -> str:
        """
        Caeser's Cipher used on a string.
        :return: Ciphered string.
        """

        result = ""

        for char in plaintext:
            # Account for spaces and special chars.
            if char not in string.ascii_letters:
                result += char
            elif char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result

    def bruteforce(self, ciphered_text: str) -> list:
        bf_results = []
        for i in range(1, 26):
            bf_results.append(self.encode(plaintext=ciphered_text, shift=i))
        return bf_results
