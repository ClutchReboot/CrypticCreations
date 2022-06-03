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

    def test_character_is_ascii_true(self):
        """
        Result is capitalized.
        """
        test = Tools().is_ascii_letter(character='a')
        self.assertEqual(test,  True)

    def test_character_is_ascii_false(self):
        """
        Result is capitalized.
        """
        test = Tools().is_ascii_letter(character='1')
        self.assertEqual(test, False)

    def test_character_is_not_ascii_true(self):
        """
        Result is capitalized.
        """
        test = Tools().is_not_ascii_letter(character='1')
        self.assertEqual(test,  True)

    def test_character_is_not_ascii_false(self):
        """
        Result is capitalized.
        """
        test = Tools().is_not_ascii_letter(character='a')
        self.assertEqual(test, False)


if __name__ == '__main__':
    unittest.main()
