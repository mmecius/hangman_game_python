import graphics

def choose_difficulty():
    difficulty = input("Enter difficulty: E-Easy, M-Medium, H-Hard: ")
    while difficulty not in "EMH":
        print("Enter difficulty: E-Easy, M-Medium, H-Hard")
        difficulty = input().upper()
    if difficulty == "E":
        print("You chosed easy level.")
    if difficulty == "M":
        del graphics.HANGMAN_PICS[8]
        del graphics.HANGMAN_PICS[7]
        print(len(graphics.HANGMAN_PICS))
    if difficulty == "H":
        del graphics.HANGMAN_PICS[8]
        del graphics.HANGMAN_PICS[7]
        del graphics.HANGMAN_PICS[5]
        del graphics.HANGMAN_PICS[3]
        print(len(graphics.HANGMAN_PICS))

choose_difficulty()