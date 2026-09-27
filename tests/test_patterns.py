import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from patterns import (
    analyse_patterns,
    detect_keyboard_patterns,
    detect_number_suffix,
    detect_repeated_characters,
    detect_sequences,
    detect_symbol_suffix,
)


def test_repeated_characters_require_three_consecutive_matches():
    assert detect_repeated_characters("aa") == []
    assert detect_repeated_characters("aaaa") == [
        "Repeated character 'a' found 4 times consecutively."
    ]


def test_detects_ascending_sequences():
    assert detect_sequences("abc") == [
        "Sequential characters detected: 'abc'."
    ]


def test_detects_reversed_sequences():
    assert detect_sequences("cba") == [
        "Reversed sequence detected: 'cba'."
    ]


def test_keyboard_patterns_are_case_insensitive():
    assert detect_keyboard_patterns("QwErTy") == [
        "Keyboard pattern detected: 'qwerty'."
    ]
    assert detect_keyboard_patterns("not-a-keyboard-pattern") == []


def test_detects_number_suffix_only_at_password_end():
    assert detect_number_suffix("password123") == [
        "Number suffix detected: '123'."
    ]
    assert detect_number_suffix("pass123word") == []


def test_detects_symbol_suffix_only_at_password_end():
    assert detect_symbol_suffix("password!!") == [
        "Symbol suffix detected: '!!'."
    ]
    assert detect_symbol_suffix("pass!word") == []


def test_detects_multiple_patterns_in_one_password():
    assert analyse_patterns("qWeRTy111!") == [
        "Repeated character '1' found 3 times consecutively.",
        "Keyboard pattern detected: 'qwerty'.",
        "Symbol suffix detected: '!'.",
    ]


def test_returns_no_patterns_for_password_without_detectable_patterns():
    assert analyse_patterns("aB7x") == []
