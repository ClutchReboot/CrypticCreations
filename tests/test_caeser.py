import unittest

from CrypticCreations.ciphers import Caeser


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = Caeser().encode(plaintext="This is testing spaces!?", shift=5)
        self.assertIn(' ',  test)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = Caeser().encode(plaintext="This is testing special characters!?.", shift=5)
        self.assertIn('!?.', test)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = Caeser().encode(plaintext="Test.", shift=5)
        self.assertEqual(test, 'Yjxy.')

    def test_allow_negative_shift(self):
        """
        Confirm expected output.
        """
        test = Caeser().encode(plaintext="Test.", shift=-5)
        self.assertEqual(test, 'Ozno.')

    def test_plaintext_exist_in_bruteforce(self):
        """
        Confirms plaintext string exists in the bruteforce return list.
        """
        test = Caeser().encode(plaintext="Test.", shift=4)
        bf_results = Caeser().bruteforce(ciphered_text=test)
        self.assertIn("Test.", bf_results)


if __name__ == '__main__':
    unittest.main()
