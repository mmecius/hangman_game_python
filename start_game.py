game_start_msg = input("Would you like to play Hangman? Choose 'yes' or 'no'")

def game_start():
    if game_start_msg == "yes":
        print("Starting the game!")
    else:
        print("Game is not starting!")

def hi_player():
    while True:
        name = input("\nPlease enter your name: ").strip()
        if name == "":
            print("Please enter your name: ")
        else:
            print("Your name is " + name.title())
            continue