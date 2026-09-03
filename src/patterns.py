KEYBOARD_PATTERNS = [
    "qwerty",
    "asdfgh",
    "zxcvbn",
    "qaz",
    "wsx",
    "edc",
    "rfv",
    "tgb",
    "yhn",
    "ujm",
]


def detect_repeated_characters(password):
    """Detect characters repeated three or more times consecutively."""

    if not password:
        return []

    patterns = []
    count = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
        else:
            if count >= 3:
                character = password[i - 1]

                patterns.append(
                    f"Repeated character '{character}' "
                    f"found {count} times consecutively."
                )

            count = 1

    if count >= 3:
        character = password[-1]

        patterns.append(
            f"Repeated character '{character}' "
            f"found {count} times consecutively."
        )

    return patterns


def detect_repeated_groups(password):

    if len(password) < 4:
        return []

    patterns = []

    for group_length in range(2, (len(password) // 2) + 1):

        if len(password) % group_length != 0:
            continue

        group = password[:group_length]
        repetitions = len(password) // group_length

        if group * repetitions == password:
            patterns.append(
                f"Repeated group '{group}' "
                f"found {repetitions} times."
            )

            break

    return patterns


def detect_sequences(password):

    if len(password) < 3:
        return []

    patterns = []

    for i in range(len(password) - 2):

        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        if second - first == 1 and third - second == 1:
            sequence = password[i:i + 3]

            patterns.append(
                f"Sequential characters detected: '{sequence}'."
            )

        elif second - first == -1 and third - second == -1:
            sequence = password[i:i + 3]

            patterns.append(
                f"Reversed sequence detected: '{sequence}'."
            )

    return patterns


def detect_keyboard_patterns(password):

    if not password:
        return []

    password_lower = password.lower()
    patterns = []

    for keyboard_pattern in KEYBOARD_PATTERNS:

        if keyboard_pattern in password_lower:
            patterns.append(
                f"Keyboard pattern detected: '{keyboard_pattern}'."
            )

    return patterns


def detect_alternating_patterns(password):

    if len(password) < 6:
        return []

    patterns = []

    for i in range(len(password) - 5):

        group = password[i:i + 2]
        remaining = password[i:]

        if group * (len(remaining) // 2) == remaining:

            repetitions = len(remaining) // 2

            if repetitions >= 3:
                patterns.append(
                    f"Alternating pattern detected: "
                    f"'{group}' repeated {repetitions} times."
                )

                break

    return patterns


def detect_capitalisation_patterns(password):

    if not password:
        return []

    patterns = []

    if password.isupper():
        patterns.append(
            "Entire password is uppercase."
        )

    elif password.islower():
        patterns.append(
            "Entire password is lowercase."
        )

    elif (
        password[0].isupper()
        and password[1:].islower()
    ):
        patterns.append(
            "Password uses capitalisation of "
            "the first character only."
        )

    if len(password) >= 4:

        alternating = True

        for i in range(1, len(password)):

            if (
                password[i].isupper()
                == password[i - 1].isupper()
            ):
                alternating = False
                break

        if alternating:
            patterns.append(
                "Alternating uppercase and lowercase "
                "pattern detected."
            )

    return patterns


def detect_number_suffix(password):

    if not password:
        return []

    index = len(password)

    while (
        index > 0
        and password[index - 1].isdigit()
    ):
        index -= 1

    if index == len(password):
        return []

    numbers = password[index:]

    return [
        f"Number suffix detected: '{numbers}'."
    ]


def detect_symbol_suffix(password):

    if not password:
        return []

    index = len(password)

    while (
        index > 0
        and not password[index - 1].isalnum()
    ):
        index -= 1

    if index == len(password):
        return []

    symbols = password[index:]

    return [
        f"Symbol suffix detected: '{symbols}'."
    ]


def analyse_patterns(password):

    patterns = []

    patterns.extend(
        detect_repeated_characters(password)
    )

    patterns.extend(
        detect_repeated_groups(password)
    )

    patterns.extend(
        detect_sequences(password)
    )

    patterns.extend(
        detect_keyboard_patterns(password)
    )

    patterns.extend(
        detect_alternating_patterns(password)
    )

    patterns.extend(
        detect_capitalisation_patterns(password)
    )

    patterns.extend(
        detect_number_suffix(password)
    )

    patterns.extend(
        detect_symbol_suffix(password)
    )

    return patterns