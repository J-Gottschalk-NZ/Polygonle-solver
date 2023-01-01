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
            
    # all_words.sort()
    return all_words

# find duplicate characters and return which characters are duplicates
def find_duplicate(word):
    
    is_duplicate = []
      
    for char in word :
        counts=word.count(char)
        
        if counts > 1 and char not in is_duplicate:
            is_duplicate.append(char)
            
    print("Duplicates", is_duplicate)
    return is_duplicate

# get index of letters in word
# https://www.sololearn.com/discuss/2226938/aside-from-index-method-how-u-can-get-the-unique-indexes-of-duplicate-characters-in-a-string-or-list
def find_index(word, letter):
    index_list = []
    for i in range(len(word)):
        if word[i] == letter:
            index_list.append(i)
            
    return index_list    


# iterate through string and find index and letter 
# returns list of the index and letter for yellow / green letters
def get_indices(color):
    # get indices
        indices_list = []

        color_index = 0
        for letter in color:
            
            color_row = []
            if letter != "-":
                
                # add to must have list!
                must_have.append(letter)
                
                # add to index row
                color_row.append(color_index)
                color_row.append(letter)
                
                # add entry to indices
                indices_list.append(color_row)
            
            color_index += 1   
        
        return indices_list


def yellow_green_remover(color, color_index_list):
    
    # Remove words with letters in the wrong place                        
    for i in color_index_list:
        color_row = i[0]
        color_letter = i[1]
        
        for item in right_length.copy():
            
            try:
                # remove words where yellow letters in wrong place
                if color == "yellow" and item[color_row] == color_letter:
                    right_length.remove(item)
                
                # remove words which don't have green letters in correct place
                elif color == "green" and item[color_row] != color_letter: 
                    right_length.remove(item)
                    
            # except IndexError:
            #     pass
            except ValueError:
                pass
                
    return None



# get words from list...
all_words = get_all_words()


new_puzzle = ""
while new_puzzle == "":
    must_have = []
    right_length = []

    pattern = input("Enter pattern (eg 12231)")

    # get word length and get all valid words from word list
    word_length = len(pattern)
    unique_letters = len(set(pattern))

    suggested =  ""

    if word_length == 8:
        suggested = "asteroid"
    elif word_length == 9:
        suggested = "relations"
    elif word_length == 10:
        suggested = "redactions"
    elif word_length == 7:
        suggested = "slarted"
        
    print(suggested)

    for word in all_words:
        
        if len(set(word)) == unique_letters and len(word) == word_length:
            right_length.append(word)
        
    duplicate_chars = find_duplicate(pattern)
    for item in duplicate_chars:
        
        # find list of indices for the letter
        find_indices = find_index(pattern, item)
        
        if len(find_indices) > 1:
            a =  find_indices[0]
            b = find_indices[1]
        
        # remove non-matching words from list
        if len(find_indices) == 2:
            
            for item in right_length.copy():
                if item[a] != item[b]:
                    right_length.remove(item)
        
        elif len(find_indices) == 3:
            c = find_indices[2]
            
            for item in right_length.copy():
                if not(item[a] == item[b] == item[c]):
                    right_length.remove(item)
                    
    print("Right lenght", len(right_length))

    show_words = input("Show possible words? ").lower()
    if show_words == "yes" or show_words == "y":
        print(right_length)

    again = ""
    while again == "": 
                        
        not_in = input("What letters are NOT in the word? ").lower()

        # remove letters that are not in the word
        for letter in not_in:

            for item in right_length.copy():
                if letter in item:
                    right_length.remove(item)
                    

        # remove letters that are in the wrong place (yellow)
        yellow = input("What letters are in the wrong place?  eg: T---E means the T and E are in the word but in the wrong place.  Press <enter> if you don't have any yellow letters. ")

        green = input("Which letters are in the right place. eg: T---- means the T is in the right place Press <enter> if you don't have any green letters.  ")

        # only execute this code if we have yellow letters!
        if yellow != "":        
            # get index / letter for yellow letters
            yellow_indices = get_indices(yellow)
            
            # remove words that have yellow letters in wrong place
            yellow_green_remover("yellow", yellow_indices)
            
        if green != "":
            green_indices = get_indices(green)
            
            # remove words that don't have green letter in right place
            yellow_green_remover("green", green_indices)

        # remove words which don't contain yellow letters
        for item in right_length.copy():    
            for letter in must_have:
                if letter not in item:
                    
                    # sometimes it tries to remove a word that is not in the list anymore.  In that case we want to just keep going instead of crashing.
                    try:
                        right_length.remove(item)  
                    except ValueError:
                        pass  


        print(right_length)
        
        again = input("Press <enter> to keep going or any key to keep solving")
    
    print()    
    new_puzzle = input("Press <enter> to solve a new puzzle or any key to quit ")
    print()
    
print("Thanks for playing!")