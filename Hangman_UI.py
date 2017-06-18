# Hangman game
#

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed=0
    for items in lettersGuessed:
        for letters in secretWord:
            if items==letters:
                guessed+=1
    if guessed>=len(secretWord):
        return True
    else:
        return False
     
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word=''
    for letters in secretWord:
        if letters in lettersGuessed:
            guessed_word+=letters
            guessed_word+=' '
        else:
            guessed_word+="_ "
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    total=string.ascii_lowercase
    result=''
    for letters in total:
        if letters not in lettersGuessed:
            result+= letters
    return result

def play_round_UI(roundn,secretWord,inputletter):
    ent_guess.delete(0,1)	
    if inputletter in roundn[1]:
        lbl_message.configure(text="Oops! You've already guessed that letter") 
    else:
        if inputletter in secretWord:
            roundn[1]+=inputletter
            lbl_message.configure(text='Good guess')
            lbl_guess.configure(text='%s' % getGuessedWord(secretWord, roundn[1]))
            lbl_guessleft.configure(text='You have %s guesses left.' % str(roundn[0]))
            lbl_letterleft.configure(text='%s' % getAvailableLetters(roundn[1]))
        else:
            roundn[0]-=1
            roundn[1]+=inputletter
            lbl_message.configure(text='Oops! That letter is not in my word')
            lbl_guess.configure(text='%s' % getGuessedWord(secretWord, roundn[1]))
            lbl_guessleft.configure(text='You have %s guesses left.' % str(roundn[0]))
            lbl_letterleft.configure(text='%s' % getAvailableLetters(roundn[1]))
    if roundn[0]==0:
        lbl_message.configure(text='Sorry, you ran out of guesses. The word was %s.' %(secretWord))
        btn.configure(state='disabled')
    elif isWordGuessed(secretWord, roundn[1]):
        lbl_message.configure(text='Congratulations, you won!')
        btn.configure(state='disabled')
        
def hangman_UI():
    secretWord = chooseWord(wordlist).lower()
    nb_guesses=8
    lettersGuessed=[]
    roundn=[nb_guesses,lettersGuessed]
    lbl_guess.pack()
    lbl_guessleft.pack()
    lbl_letterleft.pack()
    ent_guess.pack()
    btn.pack()
    lbl_guess.configure(state='normal')
    lbl_guess.configure(text='%s' % getGuessedWord(secretWord, roundn[1]))
    lbl_guessleft.configure(state='normal')
    lbl_guessleft.configure(text='You have %s guesses left.' % str(roundn[0]))
    lbl_letterleft.configure(text='%s' % getAvailableLetters(roundn[1]))
    btn.configure(text="Validate your guess")
    btn.configure(state='active')
    btn.configure(command= lambda: play_round_UI(roundn,secretWord,ent_guess.get()))
    btn.pack()
    lbl_message.pack()

    
def save_name():
    username = ent_name.get()
    btn_name.configure(state='disabled')
    ent_name.configure(state='disabled')
    btn_start.configure(state='normal')
    btn_start.configure(text="Let's play %s" % username)
    btn_start.pack()

import tkinter as tk

window = tk.Tk()
window.title("Hangman")
window.geometry("600x600")
nb_guesses=8
lettersGuessed=[]
roundn=[nb_guesses,lettersGuessed]
secretWord=""
lbl_welcome = tk.Label(window, text="Welcome to the game, Hangman!")
lbl_welcome.pack()
ent_name= tk.Entry(window)
ent_name.pack()
btn_name = tk.Button(window, text="save your name", command=save_name)
btn_name.pack()
btn_start= tk.Button(window, state='disabled', command=hangman_UI)
lbl_guess = tk.Label(window, state='disabled')
lbl_guessleft = tk.Label(window, state='disabled')
lbl_letterleft = tk.Label(window, state='disabled')
lbl_message = tk.Label(window, text="", state='disabled')
ent_guess= tk.Entry(window)
btn = tk.Button(window, state='disabled')
window.mainloop()


#game_session()



