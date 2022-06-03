import unittest

from CrypticCreations.ciphers import *


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = Rot13Cipher(text="This is testing spaces!?").encipher()
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = Rot13Cipher(text="This is testing special characters!?.").encipher()
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = Rot13Cipher(text="Test.").encipher()
        self.assertEqual(test, 'Grfg.')

    def test_bruteforce_expected_output(self):
        """
        Confirm expected output.
        """
        test = Rot13Cipher(text="Grfg.").bruteforce()
        self.assertEqual(test, ['Test.'])


if __name__ == '__main__':
    unittest.main()
