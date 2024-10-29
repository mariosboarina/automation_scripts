import random
import string
import pyperclip

LENGTH = 12
INCLUDE_DIGITS = True
INCLUDE_SPECIAL_CHARS = True
INCLUDE_UPPERCASE = True

def generate_password(length=12, include_digits=True, include_special_chars=True, include_uppercase=True):
    """
    Genera una password
    - length (int): lunghezza password
    - include_uppercase (bool): includere lettere maiuscole (altrimenti solo minuscole)
    - include_digits (bool): includere caratteri numerici
    - include_special_chars (bool): includere caratteri speciali
    """
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


pyperclip.copy(generate_password(length=LENGTH,
                                 include_digits=INCLUDE_DIGITS,
                                 include_special_chars=INCLUDE_SPECIAL_CHARS,
                                 include_uppercase=INCLUDE_UPPERCASE))


