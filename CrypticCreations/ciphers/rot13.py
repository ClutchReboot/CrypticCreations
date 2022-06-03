import string


class Rot13Cipher:
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
            # Account for spaces and special chars.
            if char not in string.ascii_letters:
                result += char
            elif char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result

    def bruteforce(self) -> list:
        """
        Used to get a list every possible cipher for the input ciphered_text.
        Since shift is hard coded, there is only 1 item returned in the list.
        """

        return [self.encipher()]

    # TODO: Create decipher function that accepts self.creation_type value from Creations Class
