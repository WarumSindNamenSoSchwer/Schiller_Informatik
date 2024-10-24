import sys
import random
import turtle

def self_destruct():
    print("Closing the program. Goodbye!")
    sys.exit()

def encrypt_word(word, enc_list, word_list, dev_Opt=None):
    for index in word:
        enc_list.append('_')
        word_list.append(index)
    if dev_Opt == 1:    
        print( word,enc_list,word_list)

def read_word_from_list(path):
    with open(path) as f:
        words_list = f.readlines()
        words_list = [x.strip() for x in words_list]
    return words_list

def shuffle_list_1word(words_list):
    random.shuffle(words_list)
    return words_list[0]

WIN_TITLE = "You won somehow"
WIN_TEXT = "Wanna Play again? Yes/No"
LOSS_TITLE = "You lost Dumbo"
LOSS_TEXT = "Wanna Play again? Yes/No"

def check_game_state(enc_list, tries, check_, win_or_loss = None):
    if win_or_loss == None:
        title = WIN_TITLE
        text = WIN_TEXT
    elif win_or_loss == 1:
        title = LOSS_TITLE
        text = LOSS_TEXT

    if check_:
        if '_' not in enc_list:
            replay_Opt = turtle.textinput(title, text)
            if replay_Opt.lower() == "yes" or replay_Opt.lower() == "y":
                print(tries)  # Debug-Ausgabe
                return True
            elif replay_Opt.lower() == "no" or replay_Opt.lower() == "n":
                self_destruct()
                return False
    elif check_ == False:
        replay_Opt = turtle.textinput(title, text)
        if replay_Opt.lower() == "yes" or replay_Opt.lower() == "y":
            print(tries)  # Debug-Ausgabe
            return True
        elif replay_Opt.lower() == "no" or replay_Opt.lower() == "n":
            self_destruct()
            return False