import random, time
from PyDictionary import PyDictionary

#import functions
import graphics
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


play_again = True
while play_again:
    words_list.chosen_word
    guess = []
    guessed_letters = []
    blank_word = []
    for letter in words_list.chosen_word:
        blank_word.append("_")
    attempts = 6
    
    while attempts > 0:

        if (attempts !=0 and "_" in blank_word):
            print(("\nYou have {} attempts remaining.").format(attempts))

        try:
            guess = str(input("\nPlease type in a letter from A-Z:")).lower()
        except:
            print("That is not valid input. Please try again.")
            continue

        else:
            if not guess.isalpha():
                print("That is not a letter. Please try again.")
                continue

            elif len(guess) > 1:
                print("That is more than one letter. Please try again.")
                continue

            elif guess in guessed_letters:
                print("You have already guessed that letter. Please try again.")
                continue
            else:
                pass

            guessed_letters.append(guess)

            if guess not in words_list.chosen_word:
                attempts -= 1
                print(graphics.HANGMAN_PICS[(len(graphics.HANGMAN_PICS)-1) - attempts])
            else:
                search_more = True
                start_search_index = 0
                while search_more:
                    try:
                        found_at_index = words_list.chosen_word.index(guess, start_search_index)
                        blank_word[found_at_index] = guess
                        start_search_index = found_at_index + 1
                    except:
                        search_more = False
                        
            print("".join(blank_word))

            if attempts == 0:
                print("Sorry, the game is over. The word was " + words_list.chosen_word)
                try:
                    myDict = PyDictionary(words_list.chosen_word)
                    print(myDict.getMeanings())
                except:
                    print("Not found")
                print("\nWould you like to play again?")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("Thanks for playing Hangman!")
                break

            if "_" not in blank_word:
                print("Congratulation! " + words_list.chosen_word.title() + " was the word.")
                try: 
                    myDict = PyDictionary(words_list.chosen_word)
                    print(myDict.getMeanings())
                except:
                    print("Not found")
                print("Would you like to play again?")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("Thanks for playing Hangman!")
                break

             




