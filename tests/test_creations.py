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
        test = CrypticCreations.CipherCreation(text="This is testing spaces!?")
        test.caeser(shift=5)
        self.assertIn(' ',  test.creation)

    def test_has_special_chars(self):
        """
        Does not remove special characters.
        """
        test = CrypticCreations.CipherCreation(text="This is testing special characters!?.")
        test.caeser(shift=5)
        self.assertIn('!?.', test.creation)

    def test_caeser_expected_output(self):
        """
        Confirm expected output.
        """
        test = CrypticCreations.CipherCreation(text="Test.")
        test.caeser(shift=5)
        self.assertEqual(test.creation, 'Yjxy.')

    def test_plaintext_exists_in_bruteforce(self):
        """
        Confirm initial plaintext shows up in bruteforce results.
        """
        test = CrypticCreations.CipherCreation(text="Test.")
        test.caeser(shift=5)
        bf_results = test.caeser_bf()
        self.assertIn("Test.", bf_results)

    def test_rot13_expected_output(self):
        """
        Confirm expected output.
        """
        test = CrypticCreations.CipherCreation(text="Test.")
        test.rot13()
        self.assertEqual(test.creation, 'Grfg.')

    def test_affine_default_expected_output(self):
        """
        Basic Affine test.
        """
        test = CrypticCreations.CipherCreation(text="Test.")
        test.affine()
        self.assertEqual(test.creation, 'Pwmp.')

    def test_affine_options_expected_output(self):
        """
        Affine test using options a_shift and b_shift.
        """
        test = CrypticCreations.CipherCreation(text="Test.")
        test.affine(a_shift=3, b_shift=9)
        self.assertEqual(test.creation, 'Ovlo.')


if __name__ == '__main__':
    unittest.main()
