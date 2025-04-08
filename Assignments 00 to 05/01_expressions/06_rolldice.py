import random
def roll_dice():

    while True:
    
                 
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)

            print(f"Roll 1: {roll_1}")
            print(f"Roll 2: {roll_2}")

            total = roll_1 + roll_2
            print(f"Total: {total}")
            if input("Roll again? (y/n): ").strip().lower() not in  ['y','Yes','yes','yeah']:
                break

roll_dice()    