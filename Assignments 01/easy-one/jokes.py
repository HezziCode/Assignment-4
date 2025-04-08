import pyjokes  

def joke_generator():

    print("\n🤣 Welcome to the Joke Generator! 🤣")

    user = input("\n😂 Do you want to hear a joke? (yes/no): ").strip().lower()  
 
    joke = pyjokes.get_joke()  


    if user == "yes":  
        print("\n🎭 Here's a joke for you:\n")  
        print(f"👉 {joke} 😆\n")  
    else:  
        print("\n🙃 No worries! Maybe next time.\n")  

joke_generator()