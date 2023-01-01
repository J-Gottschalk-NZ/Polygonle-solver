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
        
keep_going = ""
while keep_going == "":

    again = ""
    while again == "":
        if unique_letters == word_length:
            break
        
        a = int(input("position of first letter in pair"))        
        b = int(input("position in second letter of pair"))
        
        for item in right_length.copy():
            if item[a] != item[b]:
                right_length.remove(item)
                
        again = input("Press enter for another pair, any key to continue")
            
    not_in = input("What letters are NOT in the word? ").lower()

    # remove letters that are not in the word
    for letter in not_in:

        for item in right_length.copy():
            if letter in item:
                right_length.remove(item)

            
    print(right_length)
    
    keep_going = input("Again press enter or any key to quit")