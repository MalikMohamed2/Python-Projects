import random

rock = "🪨"
paper = "📃"
scissors = "✂️"

game_images = [rock, paper, scissors]

user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "
)

if not user_choice.isdigit():
    print("You Type an invalid number. You Lose!😔")
    exit()

user_choice = int(user_choice)

if user_choice < 0 or user_choice > 2:
    print("You Type an invalid number. You Lose!😔")
    exit()

print("You chose:")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!😎")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!😔")
elif user_choice > computer_choice:
    print("You Win!😎")
elif user_choice < computer_choice:
    print("You Lose!😔")
else:
    print("It's a Draw!😃")
