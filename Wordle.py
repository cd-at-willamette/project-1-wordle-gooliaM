########################################
# Name: Julia Martin
# Collaborators (if any): ChatGPT
# GenAI Transcript (if any): I used ChatGPT a lot to understand how it worked- the transcript is long so I can email it if you ask
# Estimated time spent (hr): 2.5
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

#This def checks if the given word from get_word_from_dictionary() has repeated letters (if not, returns word to function)
def check_if_contains_rpt_letters(word):
    a = 1
    for i in range(len(word)):
        letter = word[i]
        for x in range(len(word)):
            if (letter == word[x]) and (x != i):
                a = 0
    if a > 0:
        return True
    else:
        return False

#This def retrieves a random 5 letter word from ENGLISH_WORDS and passes it to check_if_contains_rpt_letters, if it's good then it's returned to the wordle()
def get_word_from_dictionary(word):
    random.shuffle(ENGLISH_WORDS)
    for word in ENGLISH_WORDS:
        if len(word) == 5:
            if check_if_contains_rpt_letters(word) == True:
                return word

def record_input(gw):
    row = 0
    col = 0
    char = ''
    for i in range(5):
        char =  char + gw.get_square_letter(row,col)
        col = col + 1
    return char

def compare_words(char, word, gw):
    for i in range(5):
        if char[i] == word[i]:
            gw.set_square_color(0,i,"green")
        else:
            gw.show_message("Guess is incorrect")

def wordle():
    #creates the graphics window
    gw = WordleGWindow()

    #get's the random 5 letter word (uses get_word_from_dictionary <- check_if_contains_rpt_letters)
    word = ''
    word = get_word_from_dictionary(word)
    
    #checks a guess
    
    def enter_action():
        char = record_input(gw)
        compare_words(char, word, gw)
        
    gw.add_enter_listener(enter_action)
    
# Startup boilerplate
if __name__ == "__main__":
    wordle()
