from secrets import choice
from string import ascii_letters, digits


# format for randomly generated password: XXXXXX-XXXXXX-XXXXXX
# with no special characters: string of 15 chars
# string only includes letters and digits


class GeneratePassword:
    characters = ascii_letters + digits

    @staticmethod
    def __regular_generation():
        password = "-".join(
            "".join(choice(GeneratePassword.characters) for i in range(6))
            for i in range(3)
        )

        return password

    @staticmethod
    def __no_special_chars():
        password = "".join(choice(GeneratePassword.characters) for i in range(15))

        return password

    @staticmethod
    def generate(noSpecialChars=False):
        return (
            GeneratePassword.__no_special_chars()
            if noSpecialChars
            else GeneratePassword.__regular_generation()
        )
