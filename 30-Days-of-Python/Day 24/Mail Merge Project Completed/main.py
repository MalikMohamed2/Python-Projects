PLACEHOLDER = "[name]"


with open(
    "F:/Malek/Malek Python/Day 24/Mail Merge Project Completed/Input/Names/invited_names.txt"
) as names_file:
    names = names_file.readlines()

with open("F:/Malek/Malek Python/Day 24/Mail Merge Project Completed/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(
            f"F:/Malek/Malek Python/Day 24/Mail Merge Project Completed/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)
