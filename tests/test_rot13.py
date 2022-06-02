import unittest

from CrypticCreations.ciphers import ROT13


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = ROT13.encode(plaintext="This is testing spaces!?")
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = ROT13.encode(plaintext="This is testing special characters!?.")
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = ROT13.encode(plaintext="Test.")
        self.assertEqual(test, 'Grfg.')


if __name__ == '__main__':
    unittest.main()
