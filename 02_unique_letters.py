import re

# empty list to read list from a file
all_words = []
right_length = []
has_doubles = []
no_doubles = []

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
double_ups = input("Does the word have any double letters? ")

# regex to check for duplicate letters
regexp = re.compile(r"(.)\1")

for item in all_words:
    if len(set(item)) == unique_letters and len(item) == word_length:
        right_length.append(item)
        
for item in right_length:
    match = re.search(regexp, item)
    if match and double_ups == "yes":
        has_doubles.append(item)
    else:
        no_doubles.append(item)
        
print(no_doubles)