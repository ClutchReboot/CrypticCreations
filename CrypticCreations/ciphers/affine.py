class Affine:
    def __init__(self, plaintext: str, a: int, b: int):
        self.plaintext = plaintext
        self.a = a
        self.b = b
        self.inva = -1
        for i in range(1, 26, 2):
            if (self.a * i) % 26 == 1:
                self.inva = i
        assert 0 <= self.inva <= 25, 'invalid key: a='+str(a)+', no inverse exists (mod 26)'

    def encipher(self):
        result = ''
        for char in self.plaintext:
            result += chr((self.a * ord(char) + self.b - 97) % 26 - 97)
        return result
