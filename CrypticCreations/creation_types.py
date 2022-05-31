from enum import Enum


class CipherType(Enum):
    NONE = 'none'
    BASIC_CIPHER = 'basic_cipher'


class RandomType(Enum):
    NONE = 'none'
    WORD = 'word'
    SENTENCE = 'sentence'
    PARAGRAPH = 'paragraph'
    VALID_RANDOM_SPRINKLE = ['sentence', 'paragraph']
