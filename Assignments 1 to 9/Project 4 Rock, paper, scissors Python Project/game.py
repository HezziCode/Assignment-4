import random

def rock_paper_game():
    choices = ["rock", "paper", "scissors"]
    attempts = 5
    user_wins = 0
    computer_wins = 0

    while attempts > 0:
        computer_choice = random.choice(choices)
        print(f"\nYou have {attempts} attempts left.")
        
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        print(f"Computer choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("Congratulations! You win this round!")
            user_wins += 1
        else:
            print("Sorry, you lose this round!")
            computer_wins += 1

        attempts -= 1

    print("\nGame over. Thank you for playing!")
    print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")

    if user_wins > computer_wins:
        print("Overall Winner: You!")
    elif computer_wins > user_wins:
        print("Overall Winner: Computer!")
    else:
        print("It's an overall tie!")

rock_paper_game()
