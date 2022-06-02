from enum import Enum


class CipherType(Enum):
    NONE = 'none'
    CAESER_CIPHER = 'caeser_cipher'
    ROT13_CIPHER = 'rot13_cipher'


class RandomType(Enum):
    NONE = 'none'
    WORD = 'word'
    SENTENCE = 'sentence'
    PARAGRAPH = 'paragraph'
    VALID_RANDOM_SPRINKLE = ['sentence', 'paragraph']
