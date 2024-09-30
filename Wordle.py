########################################
# Name: Julia Martin
# Collaborators (if any): ChatGPT
# GenAI Transcript (if any): I used ChatGPT a lot to understand how it worked- the transcript is long so I can email it if you ask
# Estimated time spent (hr): 3.5
# Description of any added extensions:random (I can't remember if this was included or not) - choose a word at random
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
            if letter == word[x] and x != i:
                return False
    return True

#This def retrieves a random 5 letter word from ENGLISH_WORDS and passes it to check_if_contains_rpt_letters, if it's good then it's returned to the wordle()
def get_word_from_dictionary(word):
    random.shuffle(ENGLISH_WORDS)
    for word in ENGLISH_WORDS:
        if len(word) == 5:
            if check_if_contains_rpt_letters(word) == True:
                return word

#records the input that the user has written
def record_input(gw, row, col):
    char = ''
    for i in range(5):
        char =  char + gw.get_square_letter(row,col)
        col = col + 1
    return char
    
#compares the input to the chosen word, making it yellow & green as needed
def compare_words(char, word, gw, row):
    for i in range(5):
        if char[i] == word[i]:
            gw.set_square_color(row,i,CORRECT_COLOR)
        else:
            for x in range(5):
                if char[i] in word:
                    gw.set_square_color(row,i,PRESENT_COLOR)
                else:
                    gw.set_square_color(row,i,MISSING_COLOR)
                
def check_if_won(gw, char, word):
    a = 0
    for i in range(5):
        if char[i] == word[i]:
            a = a + 1
    if a == 5:
        gw.show_message("You've won!")
        

def check_if_input_is_word(gw, row, col):
    char = ''
    char = record_input(gw, row, col).lower()
    if is_english_word(char):  # Use the `is_english_word` from the `english` module
        return char.upper()
    else:
        gw.show_message(f"{char.upper()} is not a valid word.")
        return None

def wordle():
    #creates the graphics window
    gw = WordleGWindow()
    row = 0
    
    
    #get's the random 5 letter word (uses get_word_from_dictionary <- check_if_contains_rpt_letters)
    word = ''
    word = get_word_from_dictionary(word).upper()
    
    gw.show_message("Try to guess the 5 letter word! ")
    
    #checks a guess
    def enter_action(col = 0):
        nonlocal row
        char = check_if_input_is_word(gw, row, col)
        compare_words(char, word, gw, row)
        check_if_won(gw, char, word)
        row += 1
        gw.set_current_row(row)
        
        if row == 6:
            gw.show_message("Better luck next time! The word was " + word)


    gw.add_enter_listener(enter_action)


# Startup boilerplate
if __name__ == "__main__":
    wordle()
