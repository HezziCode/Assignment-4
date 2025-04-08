#  My Hand written code for hangman game

# import random

# def hang_man():
#     words = ["python", 'java', 'hangman', 'computer', 'programming']

#     word = random.choice(words)

#     incorrect_guesses = 0

#     under_score = ["_"] * len(word)

#     print("Let's play Hangman!")
#     print(" ".join(under_score))

    

#     while incorrect_guesses < 6: 
#         guess_words = str(input("Guess a word: ")).lower().strip()
#         if len(guess_words) != 1:
#             print("Please enter only one letter at a time.")
#             continue
#         if guess_words in word:
#             for i in range(len(word)):
#                 if word[i] == guess_words:
#                     under_score[i] = guess_words
#             print("Good guess!")
#         else:
#             incorrect_guesses += 1
#             print(f"Wrong guess! You have {6 - incorrect_guesses} attempts left.")

#         print(" ".join(under_score))
        
#         if "_" not in under_score:
#             print("Congratulations! You guessed the word:", word)
#             break 
#         if incorrect_guesses == 6:
#             print("Sorry, you lost! The word was:", word)
# hang_man()


# AI code for hangman game

import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def hang_man():
    words = ["python", 'java', 'hangman', 'computer', 'programming']
    word = random.choice(words)
    under_score = ["_"] * len(word)

    # 🟡 Difficulty level
    print(Fore.YELLOW + "Choose difficulty level: easy / hard")
    difficulty = input("→ ").strip().lower()
    
    if difficulty == "easy":
        max_attempts = 8
    elif difficulty == "hard":
        max_attempts = 4
    else:
        print(Fore.RED + "Invalid choice! Defaulting to 6 attempts.")
        max_attempts = 6

    incorrect_guesses = 0
    guessed_letters = []

    print(Fore.CYAN + "\nLet's play Hangman!")
    print(" ".join(under_score))

    while incorrect_guesses < max_attempts:
        guess = input(Fore.MAGENTA + "\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print(Fore.RED + "⛔ Please enter only one letter at a time.")
            continue
        if guess in guessed_letters:
            print(Fore.YELLOW + "⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    under_score[i] = guess
            print(Fore.GREEN + "✅ Good guess!")
        else:
            incorrect_guesses += 1
            print(Fore.RED + f"❌ Wrong guess! {max_attempts - incorrect_guesses} attempts left.")

        print(Fore.CYAN + "Word: " + " ".join(under_score))
        print(Fore.LIGHTBLACK_EX + f"Guessed letters: {', '.join(guessed_letters)}")

        if "_" not in under_score:
            print(Fore.GREEN + "\n🎉 Congratulations! You guessed the word:", word)
            return

    print(Fore.RED + "\n💀 Sorry, you lost! The word was:", word)

hang_man()
