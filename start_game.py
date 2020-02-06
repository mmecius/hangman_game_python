def game_start():
    print("Would you like to play Hangman? Choose 'yes' or 'no'")
    return input().lower().startswith("y")

def hi_player():
    name = input("\nPlease enter your name: ").strip()
    print("Hi " + name.title() + " time to play hangman!")