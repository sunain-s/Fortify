from secrets import choice
from string import ascii_letters, digits


# format for randomly generated password: XXXXXX-XXXXXX-XXXXXX
# with no special characters: string of 15 chars
# string only includes letters and digits


class PasswordGenerator:

    @classmethod
    def _characters(cls):
        return ascii_letters + digits

    @classmethod
    def _regular_generation(cls):
        password = "-".join(
            "".join(choice(cls._characters()) for i in range(6)) for i in range(3)
        )

        return password

    @classmethod
    def _no_special_chars(cls):
        password = "".join(choice(cls._characters()) for i in range(15))

        return password

    @classmethod
    def generate(cls, noSpecialChars=False):
        return cls._no_special_chars() if noSpecialChars else cls._regular_generation()
