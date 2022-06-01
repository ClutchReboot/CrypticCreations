import string


def caeser(plaintext: str,  shift: int) -> str:
    """
    Basic Caeser Cipher. Numbers and special characters are ignored.
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
