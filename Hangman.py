#Hangman Game
import random

potential_words = ["neigh", "cutie", "nae", "hippo"]        #can change to liking
word = random.choice(potential_words)       #randomly chooses an element from the list
word = word.lower()     #ensures word is always in lowercase
print(word)

easyword = []
current_word = []
maxfails = 6            #can change to liking
fails = 0               #starting fails

for letter in word:
    easyword.append(str(letter))        #makes an empty space for each letter in the word

for letter in word:
    current_word.append("_")            #replaces empty space with "_"


while fails < maxfails:
    print(current_word)
    guess=input('Guess a letter: ')
    guess = guess.lower()           #ensures guess is always in lowercase

    def numberOfTries(fails):
        if fails == 0:
            print("You guessed the word correctly in 1 try!")
        elif (fails + 1) > 1:
            print("You guessed the word correctly and have " + str(totalFails - 1) + " tries left!")

    if guess.isnumeric():              #ensures user's guess isn't a number
        print("Type a lower case letter please!")
    elif guess == word:
        print("Congratulations!")
        numberOfTries(fails)
        break
    elif guess in word:
        for i in range(len(word)):
            if guess== word[i]:
                current_word[i] = guess
        if current_word == easyword:
            print("Congratulations!")
            numberOfTries(fails)
            break
    else:
        fails += 1
        totalFails = maxfails - fails
        print("Try again! You have " + str(totalFails) + " tries left.")
