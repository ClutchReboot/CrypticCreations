import string


class Tools:

    @staticmethod
    def ascii_to_index(letter: str):
        return ord(letter.lower()) - 97

    @staticmethod
    def index_to_ascii(index: str, capitalize: bool = False):
        index = index % 26
        if capitalize:
            return chr(index + 65)
        return chr(index + 97)

    @staticmethod
    def is_ascii_letter(character: str):
        return character in string.ascii_letters

    @staticmethod
    def is_not_ascii_letter(character: str):
        return character not in string.ascii_letters
