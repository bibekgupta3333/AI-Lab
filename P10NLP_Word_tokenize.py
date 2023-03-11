# Import the word_tokenize function from the nltk.tokenize module
from nltk.tokenize import word_tokenize

# Import the nltk library
import nltk

# Download the necessary resources for tokenization
nltk.download('punkt')

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into individual words using the word_tokenize function
tokens = word_tokenize(sentence)

# Print the resulting list of tokens
print(tokens)
