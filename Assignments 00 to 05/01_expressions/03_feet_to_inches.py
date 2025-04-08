def feet_to_inches():
    try:
        feet = float(input("Enter the number of feet: "))
        inches = feet * 12
        print(f"{feet} feet is {inches} inches")
    except ValueError:
        print("Please enter a valid number")


feet_to_inches()