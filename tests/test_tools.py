import unittest

from CrypticCreations.ciphers.tools import Tools


class TestCipherCreations(unittest.TestCase):

    def test_ascii_to_index(self):
        """
        Ascii to index conversion.
        """
        test = Tools().ascii_to_index(letter='c')
        self.assertEqual(test,  2)

    def test_index_to_ascii(self):
        """
        Ascii to index conversion.
        """
        test = Tools().index_to_ascii(index=2)
        self.assertEqual(test,  'c')

    def test_index_to_ascii_capitalize(self):
        """
        Result is capitalized.
        """
        test = Tools().index_to_ascii(index=2, capitalize=True)
        self.assertEqual(test,  'C')


if __name__ == '__main__':
    unittest.main()
