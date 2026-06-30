alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def caesar(text, shift, direction):
    result = ""

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char

    print(f"\nResult: {result}\n")


def get_direction():
    while True:
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            return direction
        else:
            print("Please type 'encode' or 'decode' only.\n")


def get_shift():
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            return shift
        except ValueError:
            print("Please enter a valid number.\n")


def get_restart():
    while True:
        answer = input("Type 'yes' to go again or 'no' to exit:\n").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            print("Goodbye 👋")
            return False
        else:
            print("Please type 'yes' or 'no' only.\n")


# البرنامج الرئيسي
running = True

while running:
    direction = get_direction()
    text = input("Type your message:\n")
    shift = get_shift()

    caesar(text, shift, direction)

    running = get_restart()
