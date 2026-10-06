import pandas
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "nato_phonetic_alphabet.csv")

data = pandas.read_csv(file_path)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()

    if word == "EXIT":
        print("Program ended.")
        break

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("❌ Please enter letters only (no numbers or symbols).")
    else:
        print("✅ Result:", output_list)
