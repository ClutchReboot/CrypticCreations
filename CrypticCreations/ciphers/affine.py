from .tools import Tools


class Affine(Tools):
    def __init__(self, text: str, a: int = 3, b: int = 10):
        """
        Valid values for a: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
        :param text:
        :param a:
        :param b:
        """

        self.text = text
        self.a = a
        self.b = b % 26
        self.isInvalid = False
        for i in range(1, 26, 2):
            if (self.a * i) % 26 == 1:
                self.isInvalid = True
        assert self.isInvalid, f'Invalid key: a={self.a}, no inverse exists (mod 26)'

    def encipher(self):
        result = ''
        for char in self.text:
            if self.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (self.a * self.ascii_to_index(char) + self.b) % 26
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (self.a * self.ascii_to_index(char) + self.b) % 26
                result += self.index_to_ascii(index=enciphered_index)
        return result

    # TODO: Create decipher function that accepts self.creation_type value from Creations Class
