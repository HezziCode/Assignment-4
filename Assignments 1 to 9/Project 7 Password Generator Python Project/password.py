import random
import string

def generate_password():
    try:
        password_length = int(input("\n\tEnter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    include_symbols = input("Include symbols? (y/n): ").lower()
    
    if include_symbols == 'y':
        character_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        character_pool = string.ascii_letters + string.digits

    generated_chars = random.choices(character_pool, k=password_length)
    password = ''.join(generated_chars)
    print(f"Your strong password is: {password}")

generate_password()
