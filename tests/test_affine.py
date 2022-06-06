import unittest

from CrypticCreations.ciphers import *


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = AffineCipher(text="This is testing spaces!?").encipher()
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = AffineCipher(text="This is testing special characters!?.").encipher()
        self.assertIn('!?.', test)

    def test_default_expected_output(self):
        """
        Confirm expected output.
        """
        test = AffineCipher(text="Test.").encipher()
        self.assertEqual(test, 'Pwmp.')

    def test_shifts_expected_output(self):
        """
        Confirm expected output using shifts a and b.
        """
        test = AffineCipher(text="Test.", a=9, b=10).encipher()
        self.assertEqual(test, 'Zuqz.')

    def test_negative_shifts_expected_output(self):
        """
        Confirm expected output using shifts a and b.
        """
        test = AffineCipher(text="Test.", a=-9, b=-10).encipher()
        self.assertEqual(test, 'Bgkb.')

    def test_decipher_expected_output(self):
        """
        Confirm expected output when using decipher.
        """
        test = AffineCipher(text="Fwrra.").decipher()
        self.assertEqual(test, 'Hello.')


if __name__ == '__main__':
    unittest.main()
