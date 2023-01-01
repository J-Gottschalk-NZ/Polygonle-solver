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

# get words from list...
all_words = get_all_words()
right_length = []

pattern = input("Enter pattern (eg 12231)")

# get word length and get all valid words from word list
word_length = len(pattern)
unique_letters = len(set(pattern))

for word in all_words:
    
    if len(set(word)) == unique_letters and len(word) == word_length:
        right_length.append(word)
    
print("Right lenght", len(right_length))

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
            if item[a] != item[b] != item[c]:
                right_length.remove(item)
    
print(right_length)