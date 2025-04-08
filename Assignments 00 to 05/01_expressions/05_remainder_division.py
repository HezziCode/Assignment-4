def remainder_division():
    try:
        first_num = int(input("Please enter an integer to be divided: "))
        second_num = int(input("Please enter an integer to be divided: "))
        result = first_num // second_num 
        remainder = first_num % second_num 
        print(f"The result of this division is: {result} and the remainder is: {remainder}")
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")    


remainder_division()