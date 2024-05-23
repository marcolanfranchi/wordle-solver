from itertools import product

# Function to load words from a file and find possible words
def findPossibleWords(chars):
    # Load words from file
    with open('words.txt', 'r') as file:
        word_set = set(word.strip().lower() for word in file)
        word_set = {word for word in word_set if len(word) == 5}

    if len(chars) != 5:
        raise ValueError("The input list must contain exactly 5 elements.")

    letters = list('abcdefghijklmnopqrstuvwxyz')
    
    # Generate all possible combinations
    possible_combinations = product(*[char if char else letters for char in chars])
    
    # Check for valid words
    valid_words = []
    for combination in possible_combinations:
        word = ''.join(combination)
        if len(word) == 5 and word in word_set:
            valid_words.append(word)
    
    return valid_words
