import random

def play_hangman():
    words = ["apple", "banana", "grape", "orange", "mango"]
    word = random.choice(words)
    guessed_letters = []
    wrong_letters = []
    attempts = 6

    print("\n Welcome to Hangman! ")
    print("Guess the word, one letter at a time.")
    print("You have", attempts, "attempts. Good luck!\n")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word:", " ".join(display_word))
        print("Wrong letters:", " ".join(wrong_letters))
        print("Attempts left:", attempts)

        if display_word == word:
            print("\n Congrats! You guessed the word:", word)
            break

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter.\n")
            continue

        if guess in word:
            guessed_letters.append(guess)
            print(" Good guess!\n")
        else:
            wrong_letters.append(guess)
            attempts -= 1
            print(" Wrong guess!\n")

    else:
        print("\n Out of attempts! The word was:", word)

while True:
    play_hangman()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print(" Thanks for playing Hangman! Goodbye!")
        break
