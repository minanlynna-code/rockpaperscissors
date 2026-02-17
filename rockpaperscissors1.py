import random

print("Welcome to The Game...")

choices = ["rock", "scissors","paper"]

round_num = 1
user_score = 0
computer_score = 0

while round_num <= 3:
    print(f"\n--- Round {round_num} ---")
    computer_choice = random.choice(choices)

    user_choice = input("Choose (rock/scissors/paper): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    print("Computer chose:", computer_choice)

    if computer_choice == user_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You Win this round!")
        user_score += 1
    else:
        print("You Lose this round!")
        computer_score += 1

    round_num += 1

# Final Result
print("\n===== Final Result =====")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("You Won The Game!")
elif computer_score > user_score:
    print("Computer Won The Game!")
else:
    print("The Game is a Tie!")
