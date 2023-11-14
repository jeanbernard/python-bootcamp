import random
from hangman_lives import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6

# Testing
# print(chosen_word)

display = []
for _ in chosen_word:
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        if lives <= 0:
            end_of_game = True
            print("You lose!")
            print(stages[lives])
        else:
            print("already guessed letter!")
            print(stages[lives])
            lives -= 1
    else:
        idx = 0
        for letter in chosen_word:
            if letter == guess:
                display[idx] = letter
            idx += 1

        if guess not in chosen_word:
            print(f"The letter {guess} is not in the word")
            print(stages[lives])
            lives -= 1

        if lives < 0:
            end_of_game = True
            print("You lose!")

        if "_" not in display:
            end_of_game = True
            print("You win!")
            print(f"The winning word is: {''.join(display)}")
        else:
            print(display)
