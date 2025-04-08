def slice_list():
    my_list = [42, 'banana', 7.8, True, '🚀', 'Python', 99]  # Sample list

    try:
        start_index = int(input("Enter the start index: "))  
        end_index = int(input("Enter the end index: "))  

        sliced_list = my_list[start_index:end_index]  # List slicing
        print(f"📝 Sliced list: {sliced_list}")

    except ValueError:
        print("❌ Error: Please enter valid integer indices.")
    except IndexError:
        print("❌ Error: Indices out of range!")

slice_list()
