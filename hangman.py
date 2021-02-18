import words
import random
# generate random word
secret_word = words.words[random.randint(0, len(words.words) - 1)]
total_guesses = []
right_guesses = []
temp = ""
lives = 6
# test code
#print(f"The word is: {secret_word}")


while True:
    print(f"Lives: {lives}")

    if lives == 0:
        print(f"You lose. The secret word was: {secret_word}")
        break

    if temp == secret_word:
        print("You guessed the secret word !")
        break


# ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    if guess in total_guesses:
        print(f'The letter "{guess.upper()}" were already used')
        guess = input("Try a new letter: ").lower()
    print("")
    total_guesses.append(guess)

# check if the letter guessed is in the secret word

    if guess in secret_word:
        right_guesses.append(guess)
        print(f'The letter "{guess.upper()}" is in the secret word.')
    else:
        print(f'The secret word don\'t have the letter "{guess.upper()}".')
        # remove lives from wrong guesses
        lives -= 1
# generate blank spaces == len of the word and replace the right guesses.
    temp = ""
    for letter in secret_word:
        if letter in right_guesses:
            temp += letter
        else:
            temp += "_"  # generates the blank spaces

    print("Your guesses were: ")
    print(total_guesses)
    print(f"Your word is: {temp}")
    print("")
