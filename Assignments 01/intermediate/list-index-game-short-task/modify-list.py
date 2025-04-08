def modify_list():
    my_list = [42, 'banana', 7.8, True, '🚀']

    try:
        index = int(input("Enter an index of the list: "))  
        new_value = input("Enter the new value: ")  
        my_list[index] = new_value  
        print(f"Updated list: {my_list}")

    except IndexError:
        print("❌ Error: Index out of range! Please enter a valid index.")
    except ValueError:
        print("❌ Error: Please enter a valid integer index.")

modify_list()
