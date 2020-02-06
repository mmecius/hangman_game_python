import random

word_list_url = ("words.txt")
with open(word_list_url) as file_object:
    try:
        words_list = file_object.read().split()
        print(words_list)
    except:
        print('File cannot be opened:', word_list_url)
        quit()
    
chosen_word = random.choice(words_list).lower()
