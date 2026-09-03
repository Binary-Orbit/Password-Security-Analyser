import sys

from analyser import analyse_password


def get_hidden_password(prompt):
    """
    Read a password from the terminal without echoing it.
    """

    print(prompt, end="", flush=True)

    password = []

    while True:
        # reads one character from the keyboard
        character = sys.stdin.read(1)

        # pressing enter means the user has finished typing
        if character in ("\n", "\r"):
            print()
            break

        # a backspace removes the last character
        elif character in ("\b", "\x7f"):
            if password:
                password.pop()

        # adds normal characters to the password
        else:
            password.append(character)

    # joins the characters together into the final password
    return "".join(password)


def display_analysis(analysis):
    """
    Display the results of the password analysis.

    Notice that this function receives the analysis results,
    rather than the original password. This helps ensure that
    the password itself is never printed.
    """

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
    """
    Run the password security analyser.

    getpass() is used instead of input() so that the password
    is not displayed on the terminal while it is being entered.
    """

    print("Password Security Analyser")
    print("--------------------------")

    # securely requests the password without displaying it
    password = get_hidden_password("Enter password to analyse: ")

    # analyses the password
    analysis = analyse_password(password)

    # displays the analysis results - the original password is never printed
    display_analysis(analysis)


if __name__ == "__main__":
    main()