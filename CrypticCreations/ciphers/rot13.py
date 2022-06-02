import string


class ROT13:

    @staticmethod
    def encode(plaintext: str) -> str:
        """
        Caeser's Cipher used on a string.
        :return: Ciphered string.
        """

        result = ""
        shift = 13

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
        return [self.encode(plaintext=ciphered_text)]
