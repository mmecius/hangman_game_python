import random, time
from PyDictionary import PyDictionary
import graphics
import start
import words_list
import end_game

play_again = True
while play_again:
    guess = []
    guessed_letters = []
    words_list.chosen_word
    blank_word = []
    for letter in words_list.chosen_word:
        blank_word.append("_")
    len(graphics.HANGMAN_PICS)   
   
    gameMode = input('Choose a level - Easy (9 Guesses), Medium (7 Guesses) or Hard (6 Guesses) :').lower()
    if gameMode == 'easy':
        attempts = 9
    elif gameMode == 'medium':
        attempts = 7
    else:
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
                print("Sorry, the game is over. The word was " + words_list.chosen_word.upper())
                try:
                    my_dict = PyDictionary(words_list.chosen_word)
                    print(my_dict.getMeanings())
                except:
                    print("Not found")
                print("\nWould you like to play again?")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                break

            if "_" not in blank_word:
                print("Congratulation! " + words_list.chosen_word.upper() + " was the word.")
                try: 
                    my_dict = PyDictionary(words_list.chosen_word)
                    print(my_dict.getMeanings())
                except:
                    print("Not found")
                print("Would you like to play again?")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                break
end_game.bye()
             




