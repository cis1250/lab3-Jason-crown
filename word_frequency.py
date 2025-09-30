#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies


import re

# This is a function that checks if a text qualifies as a sentence.
# You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False
    # Check for starting with a capital letter
    if not text[0].isupper():
        return False
    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False
    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False
    return True

# Keep asking not stop until it gets valid sentence is given
while True:
    user_sentence = input("Enter a sentence: ")
    if is_sentence(user_sentence):
        break
    else:
        print("This does not meet the criteria for a sentence.")

# Make everything lowercase and remove all punctuation to make it easier later to use the data
cleaned = ""
for ch in user_sentence.lower():
    if ch.isalpha() or ch.isspace():
        cleaned += ch

# Split into words
words = cleaned.split()

# Two lists: one for words, one for counts
unique_words = []
counts = []

for w in words:
    if w in unique_words:
        index = unique_words.index(w)
        counts[index] += 1
    else:
        unique_words.append(w)
        counts.append(1)

# Print results
for i in range(len(unique_words)): # gets the number of unique words then with range generates the numbers then I loop it
    print(f"{unique_words[i]}: {counts[i]}") # this was just to maadd the format like : between and word and count.
    
