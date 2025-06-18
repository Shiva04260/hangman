import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# Load the word list
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    return c == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans

def getAvailableLetters(lettersGuessed):
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    lettersGuessed = []
    mistakeMade = 0
    
    while mistakeMade < 8:
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        print("-------------")
        print(f"You have {8 - mistakeMade} guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Oops! That is not a valid letter.")
            continue
        
        if guess in lettersGuessed:
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        
        else:
            lettersGuessed.append(guess)
            mistakeMade += 1
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
        
        if mistakeMade == 5:
            print("-------------")
            print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
            break

# Choose a random word from the wordlist and start the game
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
