def find_duplicate(word):
    
    is_duplicate = []
    
    x = word
    count = 0
    for char in x :
        counts=x.count(char)
        place = count
        print(char,counts, place)
        count += 1
        
        if counts > 1 and char not in is_duplicate:
            is_duplicate.append(char)
            
    return is_duplicate

# get index of letters in word
# https://www.sololearn.com/discuss/2226938/aside-from-index-method-how-u-can-get-the-unique-indexes-of-duplicate-characters-in-a-string-or-list
def find_index(word, letter):
    index_list = []
    for i in range(len(word)):
        if word[i] == letter:
            index_list.append(i)
            
    return index_list    
       
word = input("enter word: ")
test = find_duplicate(word)

print(test)

the_list = find_index(word, test[0])
print(the_list)





