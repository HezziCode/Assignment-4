import random

dice1 = 0 
dice2 = 0  

def roll_dice():
    global dice1, dice2 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

for i in range(3):
    roll_dice()
    print(f"Roll {i+1}: Dice 1 = {dice1}, Dice 2 = {dice2}")

roll_dice()