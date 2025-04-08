import math


def pythagorean_theorem():
    try:    
        ab_length = float(input("Enter the Length of side AB : "))
        ac_length = float(input("Enter the Length of side AC : "))

        bc_length  = math.sqrt(ab_length**2 + ac_length**2)
        rounded_value = round(bc_length, 2)
        print(f"The length of BC (the hypotenuse) is: {rounded_value}")
    except ValueError:
        print("Please enter a valid number")    

pythagorean_theorem()