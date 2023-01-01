import re

# empty list to read list from a file
all_words = []
right_length = []
has_doubles = []
no_doubles = []
possibles = []

# open file and read the content in a list

# words from https://github.com/tabatkins/wordle-list
with open(r'poly_words.txt', 'r') as word_list:
    for line in word_list:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        all_words.append(x)
        
word_length = int(input("how long is the word? "))        
unique_letters = int(input("How many unique letters? "))
repeated = int(input("How many sets of repeated letters? "))


for item in all_words:
    if len(set(item)) == unique_letters and len(item) == word_length:
        right_length.append(item)
        
for item in right_length:
    if item[2] == item[4] and item[3] == item[5]:
        possibles.append(item)
        
not_in = input("What letters are NOT in the word? ").lower()

# remove letters that are not in the word
for letter in not_in:

    for item in possibles.copy():
        if letter in item:
            possibles.remove(item)

        
print(possibles)