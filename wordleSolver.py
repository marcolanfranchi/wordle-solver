from itertools import product
import nltk
from nltk.corpus import words

# download english words
nltk.download('words')

# create word list of len 5 words
word_list = words.words()
word_list = [word for word in word_list if len(word) == 5]

# Function to find possible words given a list of characters
def findPossibleWords(chars=[]):
    if len(chars) != 5:
            raise ValueError("The input list must contain exactly 5 elements.")
    else:        
        # List of all letters
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # Generate all possible combinations
        possible_combinations = product(*[char if char else letters for char in chars])
        
        # Check for valid words
        valid_words = []
        for combination in possible_combinations:
            word = ''.join(combination)
            if word in word_list and len(word) == 5:
                valid_words.append(word)
        
        return valid_words
