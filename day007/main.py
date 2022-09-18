import random
# from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
display = ["_"] * word_length
lives = 6
# print(chosen_word)

while not end_of_game:
    
    guess = input("Guess a letter: ")
    # clear()
  
    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
          
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life, you have {lives} left")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
