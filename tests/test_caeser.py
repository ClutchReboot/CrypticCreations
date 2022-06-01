import unittest

from CrypticCreations import ciphers


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = ciphers.caeser(plaintext="This is testing spaces!?", shift=5)
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = ciphers.caeser(plaintext="This is testing special characters!?.", shift=5)
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = ciphers.caeser(plaintext="Test.", shift=5)
        self.assertEqual(test, 'Yjxy.')

    def test_allow_negative_shift(self):
        """
        Confirm expected output.
        """
        test = ciphers.caeser(plaintext="Test.", shift=-5)
        self.assertEqual(test, 'Ozno.')


if __name__ == '__main__':
    unittest.main()
