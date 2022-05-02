import string
import random

vowels = ["a", "e", "i", "o", "u"]

alphabet = list(string.ascii_lowercase)

basic_consonants = [letter for letter in alphabet if letter not in vowels]

additional_consonants = {
    "ck",
    "rk",
    "pr",
    "kr",
    "cr",
    "bl",
    "nl",
    "zh",
    "br",
    "bl",
    "dr",
    "st",
    "sr",
    "sh",
    "kn",
    "cn",
    "tt",
    "kk",
    "pp",
    "nn",
    "mm",
}

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
    "set",
    "son",
    "qvist",
    "øy",
    "nes",
    "tangen",
    "do",  # Some portugese guy I guess
]

name_cosmetic = ["Mc", "von ", "von der ", "van ", "de ", "del ", "de la ", "De"]


class RandomLetterBag:
    def __init__(self) -> None:
        self.start_vowel: bool = bool(random.randint(0, 1))
        self.previous_vowel: bool = self.start_vowel
        self.double_vowel: bool = False

    def get_next(self):
        if not self.previous_vowel:
            self.previous_vowel = True
            return random.choice(vowels)
        elif self.previous_vowel and not self.double_vowel:
            number = random.randint(0, 100)
            if number > 75:
                self.double_vowel = True
                return random.choice(vowels)

        self.previous_vowel = False
        self.double_vowel = False
        return random.choice(consonants)

    def get_name(self):
        n = random.randint(2, 5)
        name = []
        i = 0
        while i < n:
            name.append(self.get_next())
            i += 1

        if name[-1] in consonants:
            name.append(random.choice(vowels))

        return "".join(name).capitalize()

    def get_lastname(self):
        lastname = (self.get_name() + random.choice(name_endings)).capitalize()
        number = random.randint(0, 100)
        if number > 75:
            lastname = random.choice(name_cosmetic) + lastname
        return lastname


namegen = RandomLetterBag()
for _ in range(10):
    print(f"{namegen.get_name()} {namegen.get_lastname()}")
