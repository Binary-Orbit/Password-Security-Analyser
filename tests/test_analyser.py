import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from analyser import analyse_password, assess_strength


def test_password_length():

    result = analyse_password("Hello123!")

    assert result.length == 9


def test_lowercase_detection():

    result = analyse_password("hello")

    assert result.has_lowercase is True
    assert result.has_uppercase is False


def test_uppercase_detection():

    result = analyse_password("HELLO")

    assert result.has_uppercase is True
    assert result.has_lowercase is False


def test_digit_detection():

    result = analyse_password("Password123")

    assert result.has_digits is True


def test_symbol_detection():

    result = analyse_password("Password!")

    assert result.has_symbols is True


def test_whitespace_detection():

    result = analyse_password("Password 123")

    assert result.has_whitespace is True


def test_character_set_size():

    result = analyse_password("Password123!")

    assert result.character_set_size == 94


def test_entropy_calculation():

    password = "Password123!"

    result = analyse_password(password)

    expected_entropy = len(password) * math.log2(94)

    assert math.isclose(result.entropy, expected_entropy)


def test_empty_password():

    result = analyse_password("")

    assert result.length == 0
    assert result.character_set_size == 0
    assert result.entropy == 0.0


def test_whitespace_only_password():

    result = analyse_password("   ")

    assert result.has_whitespace is True
    assert result.length == 3


def test_strength_categories():

    assert assess_strength(10) == "Very Weak"
    assert assess_strength(30) == "Weak"
    assert assess_strength(50) == "Moderate"
    assert assess_strength(70) == "Strong"
    assert assess_strength(90) == "Very Strong"