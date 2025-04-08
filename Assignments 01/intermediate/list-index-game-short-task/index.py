def list_index_game():
    my_list = [42, 'banana', 7.8, True, '🚀']

    try:
        user_input = int(input("Enter an index of the list: "))  
        element = my_list[user_input]  
        print(f"Element in index {user_input} is {element}")
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")
    except ValueError:
        print("Error: Please enter a valid integer index.")

list_index_game()
