# puts words in text file into sorted list
def get_all_words():
    
    all_words = []
    # open file and read the content in a list

    # words from https://github.com/tabatkins/wordle-list
    with open('poly_words.txt', 'r') as word_list:
        for line in word_list:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            all_words.append(x)
            
    all_words.sort()
    return all_words


# get words from list...
all_words = get_all_words()

pattern = input("Enter pattern (eg 12231)")

word_length = len(pattern)
unique_letters = len(set(pattern))

print("word length", word_length)
print("unique letters", unique_letters)

