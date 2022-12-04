import re

forbidden_letters = ["I", "O", "U"]
alphabet = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "J": 8,
    "K": 9,
    "L": 10,
    "M": 11,
    "N": 12,
    "P": 13,
    "Q": 14,
    "R": 15,
    "S": 16,
    "T": 17,
    "V": 18,
    "W": 19,
    "X": 20,
    "Y": 21,
    "Z": 22,
}


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


def computeValue(immatriculation: str):
    if not isValid(immatriculation):
        return None
    else:
        first_letters, number, last_letters = [_.upper() for _ in immatriculation.split("-")]

        value = int(number)

        value += alphabet[last_letters[1]] * 999
        value += alphabet[last_letters[0]] * len(alphabet) * 999

        if last_letters > "SS":
            value -= 999

        value += alphabet[first_letters[1]] * 999 * (len(alphabet) ** 2 - 1)
        value += alphabet[first_letters[0]] * 999 * (len(alphabet) ** 2 - 1) * len(alphabet)

        if first_letters >= "SS":
            value -= 999 * (23 * 23 - 1)
        if first_letters >= "WW":
            value -= 999 * (23 * 23 - 1)

        return value
