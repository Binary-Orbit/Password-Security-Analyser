import math
from dataclasses import dataclass


# values are used to estimate the size of the character set that the password could have been generated from.
LOWERCASE_SIZE = 26
UPPERCASE_SIZE = 26
DIGIT_SIZE = 10

# ASCII symbols, there are 32 common printable symbols that aren't letters or digits
SYMBOL_SIZE = 32


@dataclass
class PasswordAnalysis:
    """
    Stores all of the results from analysing a password.

    Using a dataclass gives us one structured object containing
    all of the information we want to display later.
    """

    length: int
    has_lowercase: bool
    has_uppercase: bool
    has_digits: bool
    has_symbols: bool
    has_whitespace: bool
    character_set_size: int
    entropy: float
    strength: str


def analyse_password(password: str) -> PasswordAnalysis:
    """
    Analyse the characteristics of a password.

    The password itself is only passed into this function so that
    we can analyse it. We do not return it, print it, or store it
    in the PasswordAnalysis object.
    """

    # calculates the number of characters in the password
    length = len(password)

    # checks whether the password contains at least one character from each of the main character categories
    has_lowercase = any(character.islower() for character in password)
    has_uppercase = any(character.isupper() for character in password)
    has_digits = any(character.isdigit() for character in password)

    # symbol and whitespace handling
    has_symbols = any(
        not character.isalnum() and not character.isspace()
        for character in password
    )

    # checking for spaces, tabs, newlines etc
    has_whitespace = any(character.isspace() for character in password)

    character_set_size = 0

    if has_lowercase:
        character_set_size += LOWERCASE_SIZE

    if has_uppercase:
        character_set_size += UPPERCASE_SIZE

    if has_digits:
        character_set_size += DIGIT_SIZE

    if has_symbols:
        character_set_size += SYMBOL_SIZE
    
    # if the password contains whitespace, can add one extra category to represent it
    if has_whitespace:
        character_set_size += 1

    # calculates the theoretical entropy
    if character_set_size > 0:
        entropy = length * math.log2(character_set_size)
    else:
        entropy = 0.0

    # converts the entropy value into a strength category
    strength = assess_strength(entropy)

    return PasswordAnalysis(
        length=length,
        has_lowercase=has_lowercase,
        has_uppercase=has_uppercase,
        has_digits=has_digits,
        has_symbols=has_symbols,
        has_whitespace=has_whitespace,
        character_set_size=character_set_size,
        entropy=entropy,
        strength=strength,
    )


def assess_strength(entropy: float) -> str:
    """
    Convert theoretical entropy into an educational strength category.

    These categories are simplified for this project and should
    NOT be treated as an authoritative measure of real-world
    password security.
    """

    if entropy < 28:
        return "Very Weak"

    if entropy < 36:
        return "Weak"

    if entropy < 60:
        return "Moderate"

    if entropy < 80:
        return "Strong"

    return "Very Strong"