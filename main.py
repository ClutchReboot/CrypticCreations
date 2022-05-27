import random
import string
import re
from enum import Enum


class CreationType(Enum):
    WORD = 'word'
    SENTENCE = 'sentence'
    PARAGRAPH = 'paragraph'


class RandomCreation:
    def __init__(self) -> None:
        """
        Init creation and numerous settings.
        Variable creation is used to store the randomly created / manipulated string.
        Variable _creation_type starts with type None expects one of 3 values. word, sentence, paragraph
        """

        self.creation: str = ''
        self.creation_type: CreationType = ''
        self._vowels: str = "aeiou"
        self._punctuation: str = ".....!?"
        self._regex_restrictions = {
            "word": '[^a-zA-Z0-9]+',
            "sentence": '[^a-zA-Z0-9.!? ]+'
        }

    def create_word(self,
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
        self.creation = ''.join(letter_array)
        self.creation_type = CreationType.WORD
        return self.creation

    def create_sentence(self,
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
                word_array.append(self.create_word(
                    capitalize=True,
                    letters=random.randint(min_word_length,
                                           max_word_length)
                ))
            else:
                word_array.append(self.create_word(letters=random.randint(min_word_length, max_word_length)))

        word_array[-1] += random.choice(self._punctuation)
        self.creation = ' '.join(word_array)
        self.creation_type = CreationType.SENTENCE
        return self.creation

    def create_paragraph(self, sentences: int = 4) -> str:
        """
        Generate paragraph made up of random words and sentences.
        """

        sentence_array = []
        for i in range(0, sentences):
            sentence_array.append(self.create_sentence(words=random.randint(3, 6)))
        self.creation = ' '.join(sentence_array)
        self.creation_type = CreationType.PARAGRAPH
        return self.creation

    def sprinkle_words(self, additional_words: list) -> str:
        """
        Add words randomly throughout self.creation.
        Intended for sentences or paragraphs.
        :param additional_words:
        :return:
        """

        valid_types = ['sentence', 'paragraph']
        if self.creation_type.value not in valid_types:
            return "Ensure creation_type is sentence or paragraph."

        additional_words = self._sanitize_list(user_input=additional_words)

        creation_array = self.creation.split(' ')
        indexes_to_replace = random.sample(range(len(creation_array)), len(additional_words))
        additional_words.reverse()

        for index, _ in enumerate(creation_array.copy()):
            if index in indexes_to_replace:
                creation_array[index] = additional_words.pop()
        self.creation = ' '.join(creation_array)
        return self.creation

    def _sanitize_string(self, user_input: str) -> str:
        """
        Remove unwanted characters based on a whitelist in self.regex_restrictions
        :param user_input: Expects sentence or paragraph.
        :return: Sanitized string.
        """

        return re.sub(self._regex_restrictions['sentence'], '', user_input)

    def _sanitize_list(self, user_input: list) -> list:
        """
        Remove unwanted characters based on a whitelist in self.regex_restrictions
        :param user_input: Expects list of words.
        :return: Sanitized list.
        """

        return [re.sub(self._regex_restrictions['word'], '', _) for _ in user_input]


if __name__ == '__main__':
    x = RandomCreation()
    print(f"{x.create_paragraph()=}")
    print(x.sprinkle_words(additional_words=['DOOM', 'MAKER', "OTHER", "THINGS"]))
