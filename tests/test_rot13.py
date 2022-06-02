import unittest

from CrypticCreations import ciphers


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = ciphers.rot13(plaintext="This is testing spaces!?")
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = ciphers.rot13(plaintext="This is testing special characters!?.")
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = ciphers.rot13(plaintext="Test.")
        self.assertEqual(test, 'Grfg.')


if __name__ == '__main__':
    unittest.main()
