
def hangmanState (wrongGuesses):
    states = {
        0: """--------\n|      |\n|\n|\n|\n|""",
        1: """--------\n|      |\n|      O\n|\n|\n|""",
        2: """--------\n|      |\n|      O\n|      |\n|\n|""",
        3: """--------\n|      |\n|      O\n|     \|\n|\n|""",
        4: """--------\n|      |\n|      O\n|     \|/\n|\n|""",
        5: """--------\n|      |\n|      O\n|     \|/\n|     /\n|""",
        6: """--------\n|      |\n|      O\n|     \|/\n|     / \ \n|"""
    }

    print(states[wrongGuesses])

def wordState (word, lettersGuessed): 
    state = ""
    for char in range (len(word)):
        if word[char] not in lettersGuessed:
            state += "_"
        else:
            state += word[char]
    return state

def validateLetter (letter,lettersGuessed):
    while len(letter) != 1 and letter.isalpha() and letter not in lettersGuessed:
        letter = input("Enter a valid letter or a letter that has not already been guessed")
    return letter

def validateWord (word):
    while (word.isalpha() != True):
        word = input("Invalid. Enter word to guess: ")
    return word

def startGame ():
    #initialise word for other player to guess
    word = input("Enter word to guess: ")
    word = validateWord(word)
    
    #start guessing letters
    wrongGuessesAllowed = 5
    wrongGuesses = 0
    lettersAlreadyGuessed = ""

    while (wrongGuesses < wrongGuessesAllowed):
        print(wordState(word,lettersAlreadyGuessed))
        guess = input("Guess a letter:")
        guess = validateLetter(guess,lettersAlreadyGuessed)
        
        #letter input has been validated so needs to be added to lettersAlreadyGuessed so it cant be guessed again
        lettersAlreadyGuessed += guess
        
        if guess not in word:
            wrongGuesses = wrongGuesses + 1
            print("Incorrect! " , wrongGuessesAllowed - wrongGuesses - 1, " remaining.")
        else:
            #check that the whole word has been completed
            check = wordState(word,lettersAlreadyGuessed)
            if "_" not in check:
                print("You win! The word was " , word , "!")
                break


startGame() # need to get it to not allow repeat guesses
