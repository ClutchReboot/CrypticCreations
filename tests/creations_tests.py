import unittest

import CrypticCreations


class TestRandomCreations(unittest.TestCase):

    def test_paragraph_has_spaces(self):
        """
        Paragraph method contains spaces.
        """
        test = CrypticCreations.RandomCreation()
        test.paragraph()
        self.assertIn(' ', test.creation)

    def test_word_has_no_spaces(self):
        """
        Word method has no spaces.
        """
        test = CrypticCreations.RandomCreation()
        test.word()
        self.assertNotIn(' ', test.creation)

    def test_sprinkled_word_exists(self):
        """
        Additional words added are present.
        """
        test = CrypticCreations.RandomCreation()
        test.paragraph()
        test.sprinkle_words(additional_words=['TEST'])
        self.assertIn('TEST', test.creation)


class TestCipherCreations(unittest.TestCase):

    def test_has_spaces(self):
        """
        Does not remove spaces.
        """
        test = CrypticCreations.CipherCreation(plaintext="This is testing spaces!?")
        test.caeser(shift=5)
        self.assertIn(' ',  test.creation)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = CrypticCreations.CipherCreation(plaintext="This is testing special characters!?.")
        test.caeser(shift=5)
        self.assertIn('!?.', test.creation)

    def test_expected_output(self):
        """
        Confirm expected output.
        """
        test = CrypticCreations.CipherCreation(plaintext="Test.")
        test.caeser(shift=5)
        self.assertEqual(test.creation, 'Yjxy.')


if __name__ == '__main__':
    unittest.main()
