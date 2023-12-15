def printMaskedWord(word, guesses):
    completed = True
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            completed = False
    return completed

name = input("What is your name? ")
print("Hello, " + name + "Time to play hangman!")
print("Start guessing...")

word = "secret"
guesses = ''
turns = 6

while turns > 0:
    
    if printMaskedWord(word, guesses):
        print ("You won")
        break

    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1 
        print ("Wrong\nYou have", + turns, "more guesses")
        if turns == 0:
            print ("You Lose")