import random
def guess_num():
    number = random.randint(1, 100)
    guesses = 5
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while guesses > 0:
        print(f"You have {guesses} guesses left.")
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number! in {5 - guesses + 1} attempts!")
            return
        
        guesses -= 1
        if guesses == 0:
            print(f"Sorry, you've run out of guesses. The number was {number}.")
            return
    print("Thanks for playing!")

guess_num()