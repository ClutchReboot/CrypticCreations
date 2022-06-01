import unittest

import CrypticCreations

# Run in terminal
# python3 -m unittest tests/*


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = CrypticCreations.CipherCreation(text="This is testing spaces!?")
        test.basic(shift=5)
        self.assertIn(' ',  test.creation)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        :return:
        """
        test = CrypticCreations.CipherCreation(text="This is testing special characters!?.")
        test.basic(shift=5)
        self.assertIn('!?.', test.creation)


if __name__ == '__main__':
    unittest.main(verbosity=3)
