import words_list
import rules

class NewGame():

    def __init__(self, name):
        self.name = name

    def game_start(self):
        print("#### Welcome to the HANGMAN game ####")
        print("Would you like to play Hangman? Choose 'yes' or 'no'")
        return input().lower().startswith("y")

    def hi_player(self):
        user_name = input("\nPlease enter your name: ").strip()
        print("Hi " + user_name.title() + " time to play hangman!")

    def number_of_words(self):
        print("Number of words in text file: ",len(words_list.words_list))
        print("Have fun!")


player = NewGame("new game")
player.game_start()
player.hi_player()
player.number_of_words()
rules.game_rul()