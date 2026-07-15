import secrets
import string


def generate_password(length, uppercase, lowercase, numbers, symbols, exclude_ambiguous=False):
    """
    Generates a secure password using Python's secrets module.
    """

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    character_sets = []

    ambiguous = "O0Il1"

    if uppercase:
        chars = string.ascii_uppercase
        if exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in ambiguous)
        character_sets.append(chars)

    if lowercase:
        chars = string.ascii_lowercase
        if exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in ambiguous)
        character_sets.append(chars)

    if numbers:
        chars = string.digits
        if exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in ambiguous)
        character_sets.append(chars)

    if symbols:
        character_sets.append("!@#$%^&*()-_=+[]{};:,.<>?/")

    if len(character_sets) < 2:
        raise ValueError("Select at least two character types.")

    # Guarantee at least one character from each selected type
    password = [secrets.choice(chars) for chars in character_sets]

    all_characters = ''.join(character_sets)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)