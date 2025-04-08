#  My code for the High-Low Game

# import random

# round_number = 5
# score = 0

# print("Welcome to the High-Low Game")
# print("--" * 20)

# for round in range(1, round_number + 1):
#     user_num: int = random.randint(1, 100)
#     computer_num: int = random.randint(1, 100)

#     print("--" * 20)
#     print(f"rounds {round_number}")
#     print("--" * 20)

#     print(f"Your number is {user_num}")

#     user_input = input("Do you think your number is higher or lower than the computer’s?: ")

#     if (
#         (user_input == "higher" and user_num > computer_num) or
#         (user_input == "lower" and user_num < computer_num)
#     ):
#         print(f"Correct guess! The computer's number was {computer_num}")
#         score += 1
#     else:
#         print(f"Incorrect guess! The computer's number was {computer_num}")
        
# print("___"* 25)

# print(f"Your final score is : {score}")






#  AI code for the High-Low Game

import random

round_number = 5
score = 0

print("🎉 Welcome to the High-Low Challenge! 🎉")
print("🔥 Test your luck and intuition! 🔥")
print("--" * 20)

for round in range(1, round_number + 1):
    user_num: int = random.randint(1, 100)
    computer_num: int = random.randint(1, 100)

    print("--" * 20)
    print(f"🚀 Round {round} of {round_number} – Let's go! 🚀")
    print("--" * 20)

    print(f"🎲 Your number is **{user_num}**!")

    user_input = input("🔮 Do you think your number is **higher** or **lower** than the computer's? ").strip().lower()

    if (
        (user_input == "higher" and user_num > computer_num) or
        (user_input == "lower" and user_num < computer_num)
    ):
        print(f"✅ Spot on! You're a **mind reader**! 🧠✨ The computer's number was **{computer_num}**.")
        score += 1
    else:
        print(f"❌ Oops! Better luck next time. The computer's number was **{computer_num}**.")

print("--" * 20)
print(f"🏆 **Game Over!** 🏆")
print(f"🎯 Final Score: **{score}** / {round_number} 🎯")
if score == round_number:
    print("🌟 **Perfect Score! You're a legend!** 🌟")
elif score >= round_number // 2:
    print("🔥 **Great Job! You’ve got skills!** 🔥")
else:
    print("😅 **Tough luck! Try again for a better score!** 😅")
print("--" * 20)


