import random

def chooseWord():
    words = ["python", "hangman", "programming", "computer", "keyboard"]
    word = random.choice(words)
    return word

def displayBlanks(word):
    blanks = "_" * len(word)
    print(blanks)
    return list(blanks)

def guessWord(word, display, guess):
    return guess in word, [guess if word[i] == guess else display[i] for i in range(len(word))]

def hangman():
    word = chooseWord()
    display = displayBlanks(word)
    tries = 6

    while True:
        guess = input("Guess a letter: ")

        correct, display = guessWord(word, display, guess)

        if correct:
            print("Correct!")
        else:
            print("Incorrect!")
            tries -= 1
            print("You have", tries, "tries left.")

        print(" ".join(display))

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        if tries == 0:
            print("Sorry, you've run out of attempts. The correct word was:", word)
            break

hangman()
