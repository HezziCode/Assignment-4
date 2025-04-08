def double_until_100():

    while True:

        try:
            user_input = int(input("\n🔢 Enter a starting number: "))
            if user_input <= 0:
                print("❌ Please enter a positive number!")
            else:
                break
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

    while user_input < 100:
        user_input *= 2
        print(f"\n➡️  {user_input}")

    print("\n✅ Process complete! The number is now 100 or greater.")


double_until_100()
