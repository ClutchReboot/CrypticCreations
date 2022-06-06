from .tools import Tools


class AffineCipher(Tools):
    def __init__(self, text: str, a: int = 3, b: int = 10):
        """
        Figures out inverse of a for decipher usage.

        :param text: String to be enciphered or deciphered.
        :param a: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
        :param b: integer
        """

        self.text = text
        self.a = a
        self.b = b % 26
        self.inverse_a = -1
        for i in range(1, 26, 2):
            if (self.a * i) % 26 == 1:
                self.inverse_a = i
        assert 0 <= self.inverse_a <= 25, f'Invalid key: a={self.a}, no inverse exists (mod 26)'

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

    def decipher(self):
        result = ''
        for char in self.text:
            if self.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = self.inverse_a * (self.ascii_to_index(char) - self.b)
                result += self.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = self.inverse_a * (self.ascii_to_index(char) - self.b)
                result += self.index_to_ascii(index=enciphered_index)
        return result
