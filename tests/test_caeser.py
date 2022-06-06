import unittest

from CrypticCreations.ciphers import *


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = CaeserCipher(text="This is testing spaces!?", shift=5).encipher()
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = CaeserCipher(text="This is testing special characters!?.", shift=5).encipher()
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = CaeserCipher(text="Test.", shift=5).encipher()
        self.assertEqual(test, 'Yjxy.')

    def test_allow_negative_shift(self):
        """
        Confirm expected output.
        """
        test = CaeserCipher(text="Test.", shift=-5).encipher()
        self.assertEqual(test, 'Ozno.')

    def test_plaintext_exist_in_bruteforce(self):
        """
        Confirms plaintext string exists in the bruteforce return list.
        """
        test = CaeserCipher(text="Test.", shift=4).encipher()
        bf_results = CaeserCipher(text=test).bruteforce()
        self.assertIn("Test.", bf_results)

    def test_decipher_expected_output(self):
        """
        Confirm decipher returns expected output.
        """
        test = CaeserCipher(text="Mjqqt.").decipher()
        self.assertIn(test, "Hello.")


if __name__ == '__main__':
    unittest.main()
