import re

forbidden_letters = ["I", "O", "U"]


def isValid(immatriculation):
    """ check that an immatriculation of format
        'XX-YYY-ZZ' where
        - XX are two letters
        - YYY are thre numbers
        - ZZ are two letters

        is valid
        """
    if not re.match("^\D{2}-\d{3}-\D{2}$", immatriculation):
        return False

    first_letters, number, last_letters = [_.upper() for _ in immatriculation.split("-")]

    if first_letters in ["WW", "SS"] or last_letters == "SS":
        return False

    for l in first_letters + last_letters:
        if l in forbidden_letters:
            return False

    return True
