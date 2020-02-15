from selenium import webdriver
import webbrowser

GAME_RULES = "https://en.wikipedia.org/wiki/Hangman_(game)"

def game_rul():
    print("Please read game rules -->")
    browser = webdriver.Chrome()
    browser.get(GAME_RULES)

game_rul()




