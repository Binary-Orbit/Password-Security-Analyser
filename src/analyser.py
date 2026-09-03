import math
import sys
from dataclasses import dataclass


def get_hidden_password(prompt):
    print(prompt, end="", flush=True)

    password = []

    while True:
        # reads one character from the keyboard
        character = sys.stdin.read(1)

        if character in ("\n", "\r"):
            print()
            break

        elif character in ("\b", "\x7f"):
            if password:
                password.pop()

        else:
            password.append(character)

    return "".join(password)


def display_analysis(analysis):
    print("\n" + "=" * 45)
    print("       PASSWORD SECURITY ANALYSER")
    print("=" * 45)

    print(f"\nPassword length: {analysis.length}")

    print("\nCharacter types:")
    print(f"  Lowercase:  {'Yes' if analysis.has_lowercase else 'No'}")
    print(f"  Uppercase:  {'Yes' if analysis.has_uppercase else 'No'}")
    print(f"  Digits:     {'Yes' if analysis.has_digits else 'No'}")
    print(f"  Symbols:    {'Yes' if analysis.has_symbols else 'No'}")
    print(f"  Whitespace: {'Yes' if analysis.has_whitespace else 'No'}")

    print("\nEntropy:")
    print(f"  Character-set size (N): {analysis.character_set_size}")

    print(
        f"  H = L × log₂(N) = "
        f"{analysis.length} × log₂({analysis.character_set_size})"
    )

    print(f"  Estimated entropy: {analysis.entropy:.2f} bits")

    print("\nEducational assessment:")
    print(f"  Strength: {analysis.strength}")

    print("\nNote:")
    print("  Entropy is a theoretical estimate.")
    print("  Human-created passwords may be much more predictable")
    print("  than the theoretical calculation suggests.")

    print("=" * 45)


def main():
    print("Password Security Analyser")
    print("--------------------------")

    password = get_hidden_password("Enter password to analyse: ")

    analysis = analyse_password(password)

    display_analysis(analysis)


if __name__ == "__main__":
    main()

LOWERCASE_SIZE = 26
UPPERCASE_SIZE = 26
DIGIT_SIZE = 10

SYMBOL_SIZE = 32


@dataclass
class PasswordAnalysis:
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
    length = len(password)

    has_lowercase = any(character.islower() for character in password)
    has_uppercase = any(character.isupper() for character in password)
    has_digits = any(character.isdigit() for character in password)

    has_symbols = any(
        not character.isalnum() and not character.isspace()
        for character in password
    )

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
    
    if has_whitespace:
        character_set_size += 1

    if character_set_size > 0:
        entropy = length * math.log2(character_set_size)
    else:
        entropy = 0.0

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
    if entropy < 28:
        return "Very Weak"

    if entropy < 36:
        return "Weak"

    if entropy < 60:
        return "Moderate"

    if entropy < 80:
        return "Strong"

    return "Very Strong"