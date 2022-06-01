import string


def rot13(plaintext: str) -> str:
    """
    ROT13 Cipher. Identical to Caeser's Cipher but the shift is hard coded as 13.
    """

    def cipher(plain_letter: str) -> str:
        """
        ROT13 Cipher used on a single character.
        :return: enciphered character
        """

        cipher_shift = 13
        if plain_letter.isupper():
            return chr((ord(plain_letter) + cipher_shift - 65) % 26 + 65)
        else:
            return chr((ord(plain_letter) + cipher_shift - 97) % 26 + 97)

    result = ""

    for char in plaintext:
        # Account for spaces and special chars.
        if char not in string.ascii_letters:
            result += char
        else:
            result += cipher(plain_letter=char)
    return result
