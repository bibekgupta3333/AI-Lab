import random

# List of words to choose from
words = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape']

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores with the same length as the word
word_progress = ['_' for i in range(len(word))]

# Set the number of incorrect guesses allowed
max_guesses = 6

# Keep track of the incorrect guesses made
incorrect_guesses = []

# Loop until the game is over
while True:
    # Print the current progress of the word
    print(' '.join(word_progress))
    
    # Get a letter from the user
    guess = input("Guess a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in incorrect_guesses or guess in word_progress:
        print("You've already guessed that letter!")
        continue
    
    # Check if the letter is in the word
    if guess in word:
        # Update the progress of the word
        for i in range(len(word)):
            if word[i] == guess:
                word_progress[i] = guess
        print("Correct!")
    else:
        # Add the letter to the list of incorrect guesses
        incorrect_guesses.append(guess)
        print("Incorrect!")
    
    # Check if the player has won
    if '_' not in word_progress:
        print("Congratulations, you've won!")
        break
    
    # Check if the player has run out of guesses
    if len(incorrect_guesses) >= max_guesses:
        print("Sorry, you've lost. The word was '{}'.".format(word))
        break
