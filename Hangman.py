print("The game has started.\nGuess the letters in this word!")
secretWord = "Palestine"
Length = len(secretWord)
guessword = []

# Initialize guessword with underscores
for i in range(Length):
    guessword.append("_")

count = 8

# Print initial state of guessword
for letter in guessword:
    print(letter, end=" ")
print()
print("There are", Length, "letters in this word.")

while str(guessword).lower() != str(list(secretWord)).lower() and count > 0:
    print("You have", count, "lives remaining!!!")
    guess = input("Enter your guess letter: ")

    # Validate the guess
    while len(guess) != 1:
        guess = input("Enter a single letter: ")

    found = False  # Flag to check if the guess is correct
    for i in range(Length):
        if guess.lower() == secretWord[i].lower():
            print(guess)
            guessword[i] = guess
            found = True

    if not found:
        count -= 1

    # Print current state of guessword without using join
    for letter in guessword:
        print(letter, end=" ")
    print()

if count == 0:
    print("You ran out of guesses.\nBetter luck next time")
else:
    print("Wow! You are correct, the word was", secretWord, "\nI will be sure to make the next one even harder")
