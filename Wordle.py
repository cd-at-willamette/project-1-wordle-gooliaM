########################################
# Name: Julia Martin
# Collaborators (if any): ChatGPT
# GenAI Transcript (if any): I used ChatGPT a lot to understand how it worked (I still don't really)- the transcript is long so I can email it if you ask
# Estimated time spent (hr): 2.5
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random


def wordle():
    
    #creates a function which iterates through each letter in a word given in the input to 'set' it to the game
    def display_word(window, word, row):
        #checks that the word is 5 chars
        if len(word) == 5:
            #col was defined with N_COLS = 5, so it knows to loop 5 times
            #how does letter work? how is it assigned the character value in the string? I can't find anything defining it in the graphics code
            for col, letter in enumerate(word):
                #something that places a predefined letter into a specified coordinate
                window.set_square_letter(row, col, letter)
    
    #the name of the window is 'gw', and it's calling the function? class? idk what it is? from the source to run everything
    gw = WordleGWindow()
    
    #calling the display_word function with syntax (windowName, word, row#)
    display_word(gw, "HELLO", 0)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
