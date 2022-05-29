import random
import string
import re
from enum import Enum


class CreationType(Enum):
    RANDOM_WORD = 'random_word'
    RANDOM_SENTENCE = 'random_sentence'
    RANDOM_PARAGRAPH = 'random_paragraph'
    VALID_RANDOM_SPRINKLE = ['random_sentence', 'random_paragraph']


class Creation:
    def __init__(self) -> None:
        """
        Init creation and numerous settings.
        Variable creation is used to store the created string that can be manipulated with different methods.
        """

        self.creation: str = ''
        self.creation_type: CreationType = ''
        self._vowels: str = "aeiou"
        self._punctuation: str = ".....!?"

    @staticmethod
    def _sanitize(user_input: str | list) -> str | list:
        """
        Remove unwanted characters based on a regex substitution.
        :param user_input: Input that may have unwanted characters.
        :return: Sanitized string or list.
        """

        if isinstance(user_input, str):
            return re.sub("[^a-zA-Z0-9.!? ]+", '', user_input)
        if isinstance(user_input, list):
            return [re.sub("[^a-zA-Z0-9]+", '', _) for _ in user_input]


class RandomCreation(Creation):
    def __init__(self) -> None:
        super().__init__()

    def word(self, letters: int = 10, capitalize: bool = False, ensure_vowels: int = random.randint(1, 3)):
        self.creation_type = CreationType.RANDOM_WORD
        self.creation = self._create_word(letters=letters, capitalize=capitalize, ensure_vowels=ensure_vowels)
        return self.creation

    def sentence(self, words: int = 6, min_word_length: int = 3, max_word_length: int = 10):
        self.creation_type = CreationType.RANDOM_SENTENCE
        self.creation = self._create_sentence(
            words=words,
            min_word_length=min_word_length,
            max_word_length=max_word_length
        )
        return self.creation

    def paragraph(self, sentences: int = 4):
        self.creation_type = CreationType.RANDOM_PARAGRAPH
        self.creation = self._create_paragraph(sentences=sentences)
        return self.creation

    def sprinkle_words(self, additional_words: list) -> str:
        """
        Add words randomly throughout self.creation.
        Validates that creation_type is either random_sentences or random_paragraphs.
        Updates self.creation.
        :param additional_words: Takes in a list of words.
        :return: self.creation
        """

        if self.creation_type.value not in CreationType.VALID_RANDOM_SPRINKLE.value:
            return "Ensure creation_type is random_sentence or random_paragraph."

        additional_words = super()._sanitize(user_input=additional_words)

        # Prevent too many additional_words from over powering smaller self.creation
        if len(additional_words) >= len(self.creation.split()):
            self.creation = ' '.join(additional_words)
            return self.creation

        creation_array = self.creation.split()
        indexes_to_replace = random.sample(range(len(creation_array)), len(additional_words))
        additional_words.reverse()

        for index, _ in enumerate(creation_array.copy()):
            if index in indexes_to_replace:
                creation_array[index] = additional_words.pop()
        self.creation = ' '.join(creation_array)
        return self.creation

    def _create_word(self,
                     letters: int = 10,
                     capitalize: bool = False,
                     ensure_vowels: int = random.randint(1, 3)
                     ) -> str:

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
                letter_array.append(random.choice(self._vowels))
            else:
                letter_array.append(random.choice(string.ascii_lowercase))
            ensure_vowels -= 1
        return ''.join(letter_array)

    def _create_sentence(self,
                         words: int = 6,
                         min_word_length: int = 3,
                         max_word_length: int = 10
                         ) -> str:

        """
        Create a sentence using the create_word method.
        Add punctuation at the end.
        """

        word_array = []
        for i in range(0, words):
            if not i:
                # Capitalize the first letter.
                word_array.append(self._create_word(
                    capitalize=True,
                    letters=random.randint(min_word_length,
                                           max_word_length)
                ))
            else:
                word_array.append(self._create_word(letters=random.randint(min_word_length, max_word_length)))

        word_array[-1] += random.choice(self._punctuation)
        return ' '.join(word_array)

    def _create_paragraph(self, sentences: int = 4) -> str:
        """
        Generate paragraph made up of random words and sentences.
        """

        sentence_array = []
        for i in range(0, sentences):
            sentence_array.append(self._create_sentence(words=random.randint(3, 6)))
        return ' '.join(sentence_array)


if __name__ == '__main__':
    x = RandomCreation()
    print(f"{x.paragraph(sentences=1)=}")
    print(f"{x.creation_type=}")
    print(x.sprinkle_words(additional_words=['DOOM', 'MAKER', "OTHER", "THINGS"]))
