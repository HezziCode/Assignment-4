def list_game():
    my_list = [42, 'banana', 7.8, True, '🚀', 'Python', 99] 
    
    while True:
        print("\n📜 Choose an operation:")
        print("1️⃣ Access an element")
        print("2️⃣ Modify an element")
        print("3️⃣ Slice the list")
        print("4️⃣ Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':  
            try:
                index = int(input("Enter the index to access: "))
                print(f"🔹 Element at index {index}: {my_list[index]}")
            except IndexError:
                print("❌ Error: Index out of range!")
            except ValueError:
                print("❌ Error: Please enter a valid integer index.")

        elif choice == '2':  
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                my_list[index] = new_value
                print(f"✅ Updated list: {my_list}")
            except IndexError:
                print("❌ Error: Index out of range!")
            except ValueError:
                print("❌ Error: Please enter a valid integer index.")

        elif choice == '3':  
            try:
                start_index = int(input("Enter start index: "))
                end_index = int(input("Enter end index: "))
                print(f"📝 Sliced list: {my_list[start_index:end_index]}")
            except ValueError:
                print("❌ Error: Please enter valid integer indices.")

        elif choice == '4':  
            print("👋 Exiting game. Thanks for playing!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")


list_game()
