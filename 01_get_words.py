# empty list to read list from a file
all_words = []
polygonal = []

# open file and read the content in a list

# words from https://github.com/tabatkins/wordle-list
with open(r'poly_words.txt', 'r') as word_list:
    for line in word_list:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        all_words.append(x)
        
initial_length = len(all_words)

for item in all_words:
    if  '-' not in item:
        polygonal.append(item.lower())
        
print(len(polygonal))

# write to file
with open("poly_words_v2.txt", "w") as f:
    for item in polygonal:
        f.write(item)
        f.write("\n")