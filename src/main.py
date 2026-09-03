from analyser import analyse_password
from analyser import analyse_password

def main():
    password = input("Enter password: ")
    result = analyse_password(password)

    print(f"Length: {result.length}")
    print(f"Lowercase: {result.has_lowercase}")
    print(f"Uppercase: {result.has_uppercase}")
    print(f"Digits: {result.has_digits}")
    print(f"Symbols: {result.has_symbols}")
    print(f"Whitespace: {result.has_whitespace}")
    print(f"Character set size: {result.character_set_size}")
    print(f"Entropy: {result.entropy:.2f} bits")
    print(f"Strength: {result.strength}")


if __name__ == "__main__":
    main()