import random
import string


class IncantationCreation:
    def __init__(self):
        self.vowels = list("aeiou")
        self.punctuation = list(".....!?")

    def create_word(self,
                    letters: int = 10,
                    capitalize: bool = False,
                    ensure_vowels: int = random.randint(1, 3)
                    ):

        """
        Generate a random word.
        Ensure some vowels are present be default.
        """

        letter_array = []
        for i in range(letters):
            if capitalize:
                capitalize = False
                letter_array.append(random.choice(string.ascii_uppercase))
            elif not ensure_vowels:
                ensure_vowels = random.randint(2, 4)
                letter_array.append(random.choice(self.vowels))
            else:
                letter_array.append(random.choice(string.ascii_lowercase))
            ensure_vowels -= 1
        return ''.join(letter_array)

    def create_sentence(self,
                        words: int = 6,
                        min_word_length: int = 3,
                        max_word_length: int = 10
                        ):

        """
        Create a sentence using the create_word method.
        Add punction at the end.
        """

        word_array = []
        for i in range(0, words):
            if not i:
                word_array.append(self.create_word(capitalize=True, letters=random.randint(min_word_length, max_word_length)))
            else:
                word_array.append(self.create_word(letters=random.randint(min_word_length, max_word_length)))

        # Add punctuation. May add options in the future.
        word_array[-1] += random.choice(self.punctuation)
        return ' '.join(word_array)

    def create_paragraph(self, sentences: int = 4):
        """
        Generate paragraph made up of random words and sentences.
        """

        sentence_array = []
        for i in range(0, sentences):
            sentence_array.append(self.create_sentence(
                words=random.randint(3, 6)
            ))
        return ' '.join(sentence_array)


if __name__ == '__main__':
    print(IncantationCreation().create_paragraph())
