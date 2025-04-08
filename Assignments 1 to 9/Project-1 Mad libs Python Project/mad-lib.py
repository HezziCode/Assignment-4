# This is a simple mad lib game where the user inputs words to create a funny story.

def mad_lib():
    person_name = input("Enter the name: ")
    job_title = input("Enter the job title: ")
    programming_language = input("Enter the programming language: ")
    animal = input("Enter the animal: ")
    expression = input("Enter the expression: ")

    print("\n🎮 The Bug That Saved the Day 🐛\n")
    print(f"""One crazy morning, {person_name}, a {job_title}, was coding a brilliant website using {programming_language}.
Suddenly, a {animal} jumped on the keyboard and typed a perfect line of code.
“{expression}!” shouted {person_name}, “This bug just fixed my whole project!”
From that day, they called it the “Code Saver”, and it became their lucky charm. 🍀""")

mad_lib()

