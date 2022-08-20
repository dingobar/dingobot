import string
import random

import click

vowels = ["a", "e", "i", "o", "u"]  # , "æ", "ø", "å"]

_alphabet = list(string.ascii_lowercase)

basic_consonants = [letter for letter in _alphabet if letter not in vowels]

additional_consonants = {
    "pr",
    "kr",
    "cr",
    "bl",
    "zh",
    "br",
    "bl",
    "dr",
    "st",
    "sh",
    "kn",
    "tt",
    "kk",
    "pp",
    "nn",
    "mm",
    "pp",
}

# These can't be at the beginning of a name (duh!!!)
mid_consonants = {"ck", "rk", "sr", "nc", "nk", "cn"}

# When they show up, we draw again so they are rarely chosen
unlikely_consonants = {"x", "z", "q", "w", "c"}

consonants = basic_consonants + list(additional_consonants)

name_endings = [
    "sen",
    "seth",
    "moen",
    "lien",
    "dal",
    "bakk",
    "stad",
    "vić",
    "ić",
    "slav",
    "set",
    "son",
    "qvist",
    "øy",
    "nes",
    "tangen",
    "do",  # Some portugese guy I guess???
    "vik",
    "viken",
    "støl",
    "fjord",
    "vatn",
    "sjø",
    "vann",
    "by",
    "land",
    "lini",
    "-sensei",
]

name_cosmetic = ["Mc", "von ", "von der ", "van ", "de ", "del ", "de la ", "De", "of "]


class NameGenerator:
    def __init__(self) -> None:
        self.previous_vowel: bool = bool(random.randint(0, 1))
        self.double_vowel: bool = False

    @staticmethod
    def _get_consonant(use_middle):
        if use_middle:
            consonant_choices = consonants + list(mid_consonants)
        else:
            consonant_choices = consonants
        choice = random.choice(consonant_choices)
        if choice in unlikely_consonants:
            choice = random.choice(consonant_choices)
        return choice

    def get_next(self, use_middle=True):
        if not self.previous_vowel:
            self.previous_vowel = True
            return random.choice(vowels)
        elif self.previous_vowel and not self.double_vowel:
            number = random.randint(0, 100)
            if number > 80:
                self.double_vowel = True
                return random.choice(vowels)

        self.previous_vowel = False
        self.double_vowel = False
        return self._get_consonant(use_middle)

    def get_name(self):
        n = random.randint(2, 8)
        name = []
        i = 0
        while i < n:
            name.append(self.get_next(i > 0))
            i += 1

        # VOILA!!! The name was made
        name: str = "".join(name)

        # Make sure it doesn't start with two of the same letter
        if name[0] == name[1]:
            # Remove double start and expand by one
            name = name[1:] + self.get_next()

        # Make sure we don't end with two of the same vowel
        # Make sure we don't end on two different consonants
        # Make sure we don't start with two vowels
        if name[-1] in consonants and name[-2] in consonants:
            if name[-1] != name[-2]:
                name = name[:-1] + self.get_next()
        if name[-1] in vowels and name[-2] in vowels:
            if name[-1] == name[-2]:
                name = name[:-1] + self.get_next()
        if name[0] in vowels and name[1] in vowels:
            name = name[1:] + self.get_next()

        return name.capitalize()

    def get_lastname(self):
        lastname = (self.get_name() + random.choice(name_endings)).capitalize()

        # If you're lucky you get some cosmetics
        number = random.randint(0, 100)
        if number > 80:
            lastname = random.choice(name_cosmetic) + lastname

        return lastname

    def get_fullname(self):
        return self.get_name() + " " + self.get_lastname()


@click.command()
@click.option("-n", default=1, help="Number of unique names to generate")
def main(n):
    for _ in range(n):
        namegen = NameGenerator()
        print(namegen.get_fullname())


if __name__ == "__main__":
    main()
