import random


choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors")

while True:

    user = input(
        "\nChoose rock, paper, scissors or quit: "
    ).lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(
        f"Score → You: {user_score} | "
        f"Computer: {computer_score}"
    )

print("\nGame ended.")