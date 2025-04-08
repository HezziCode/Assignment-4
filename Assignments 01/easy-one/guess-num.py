import random

def guess_num():
    num: int = random.randint(1, 10)  
    print("🔢 Guess the number between 1 and 10.")

    for i in range(5): 
        try: 
            user_guess = int(input("Enter your guess: "))
            
            if user_guess == num:
                print("🎉 You guessed it!")
                break
            elif user_guess > num:
                print("📈 Your guess is too high.")
            else:
                print("📉 Your guess is too low.")
        
        except ValueError:
            print("❌ Please enter a valid number.")

    else:  
        print(f"\n❌ Out of attempts! The number was {num}.")

guess_num()  
