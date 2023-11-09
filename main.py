import random
import hangman_words
from hangman_art import logo, stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
display = []

for _ in range(word_length):
    display += "_"

print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')


def hang(guess):
    global lives
    global end_of_game
    if guess in display:
        #  Check guessed letter
        print(f"You've already guessed {guess}.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word, you lose life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. the word is {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


while not end_of_game:
    guess_user = input("Guess a letter: ").lower()
    hang(guess_user)
    print(stages[lives])
