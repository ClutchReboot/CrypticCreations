import re


class Creation:
    def __init__(self) -> None:
        """
        Init creation and numerous settings.
        Variable creation is used to store the created string that can be manipulated with different methods.
        """

        self.creation: str = ''
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
