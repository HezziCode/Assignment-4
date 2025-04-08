import time
import pygame

def countdown_timer():

    try:
        user_input = int(input("Enter time in seconds: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound("alarm.wav")
    for i in range(user_input, 0, -1):
        print(i)
        time.sleep(1)
    print("⏰ Time's up!")

    sound.play()

    time.sleep(sound.get_length())

countdown_timer()
