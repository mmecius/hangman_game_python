from selenium import webdriver
import words_list
import time
import webbrowser

GAME_RULES = "https://en.wikipedia.org/wiki/Hangman_(game)"

def game_start():
    print("#### Welcome to the HANGMAN game ####")
    print("Would you like to play Hangman? Choose 'yes' or 'no'")
    return input().lower().startswith("y")

def hi_player():
    name = input("\nPlease enter your name: ").strip()
    print("Hi " + name.title() + " time to play hangman!")

def number_of_words():
    print("Number of words in text file: ",len(words_list.words_list))
    time.sleep(1)
    print("Have fun!")


time.sleep(1)
game_start()
print("Please read game rules -->")
browser = webdriver.Chrome()
browser.get(GAME_RULES)
hi_player()
number_of_words()




