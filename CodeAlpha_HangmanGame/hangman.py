import random

# List of predefined words
words = ['apple', 'banana', 'cherry', 'grape', 'mango']

# Choose a random word
word_to_guess = random.choice(words)
guessed_letters = []
tries = 6

# Display hidden word
def display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while tries > 0:
    print(f"Word: {display_word()}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter only one valid letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.")

    if all(letter in guessed_letters for letter in word_to_guess):
        print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
        break
else:
    print(f"\n💀 Game Over! The word was: {word_to_guess}")
