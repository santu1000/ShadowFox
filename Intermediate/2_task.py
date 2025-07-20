
import random
#you can use fgures to represent the hangman insted of stars if you want 
hangman = ["*", "**", "***", "****", "*****", "******", "*******"]
#you can add the desired words with hints 
words_hints = [
    ("python", "A programming language."),
    ("Shadowfox", "Best Internship Company for Beginners.")
]

word, hint = random.choice(words_hints)
guessed_letters = []
attempts = 0
max_attempts = len(hangman) - 1

print("Welcome to Hangman!")
print("Hint:", hint)

while attempts < max_attempts:
    print("Hangman Stage:", hangman[attempts])
    inword = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word:", ' '.join(inword))
    print("Guessed Letters:", ', '.join(guessed_letters))

    if '_' not in inword:
        print("\n Good Job , The word was:", word)
        break
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    if guess not in word:
        print("Wrong guess!\n")
        attempts += 1
    else:
        print("Correct guess!\n")
if attempts == max_attempts:
    print("Hangman Stage:", hangman[attempts])
    print(f"\n Game Over! The word was: {word}")
