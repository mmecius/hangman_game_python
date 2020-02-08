<<<<<<< HEAD
import words_list
import time

||||||| merged common ancestors
game_start_msg = input

=======
>>>>>>> ded7b0265bd3fe085c706dd7473ec3994a92cad5
def game_start():
    print("Would you like to play Hangman? Choose 'yes' or 'no'")
    return input().lower().startswith("y")

def hi_player():
    name = input("\nPlease enter your name: ").strip()
<<<<<<< HEAD
    print("Hi " + name.title() + " time to play hangman!")

def number_of_words():
    print("Number of words in text file: ",len(words_list.words_list))
    time.sleep(1)
    print("Have fun!")

||||||| merged common ancestors
    return "Hi " + name.title()
=======
    print("Hi " + name.title() + " time to play hangman!")
>>>>>>> ded7b0265bd3fe085c706dd7473ec3994a92cad5
