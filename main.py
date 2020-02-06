#import functions
#import graphics
import words_list
#import start_game
#import play_again
#import choose_level

#start_game.hi_player()
#functions.hi_function()
#graphics.hi_graphic()
#graphics.HANGMAN_PICS[0]
#graphics.startUp()
#functions.choose_category()
#play_again.repeat()

#choose_level.choose_difficulty()

#guess = []
#guessed_letters = []
#correct_letters = []
#missed_letters = []


#attempts = len(graphics.HANGMAN_PICS)
#print(attempts)
guessess = ""
failed = 0
for char in words_list.chosen_word:
    if char in guessess:
        print(char)
    else:
        print("_")
        failed += 1





