# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 03:07:30 2024

@author: otaka

This program is a shitty version of a autocorrect
"""

def get_dictionary_words(dict_file):
    dictionary = [] # get the dictionary terms
    for line in open(dict_file):
        line = line.replace("\n", "")
        line = line.split(",")
        dictionary.append(str(line[0]))
    return dictionary
    
def get_dictionary_with_values(dict_file):
    the = dict()
    for line in open(dict_file):
        line = line.replace("\n", "") #another disaster avoided, so far any desks were harmed in creation of this python program
        line = line.split(",")
        the[str(line[0])] = str(line[1])
    return(the)
    
def check_word(dictionary, word):
    word = str(word)
    for i in dictionary:
        i = str(i)
        if i == word:
            return True
    return False
    
def get_output(word, words, with_values, surr_keys, spacing):
    status = "NOT FOUND"
    found_values = set()
    #DROP
    count = 0
    for i in word:
        copy = word[:count] + word[count+1:]
        if copy in words:
            found_values.add(copy)
        count += 1
    #INSERT
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(word)+2):
        for letter in alphabet:
            new = word[:i] + letter + word[i:]
            if new in words:
                found_values.add(new)
    #SWAP
    for i in range(len(word)-1):
        swap = (word[:i] + word[i+1] + word[i] + word[i+2:]) # Swap letters at positions i and i+1 i think? (temp is before the i + after the i+1 and in tetween we add the i+1 and i in the middle)
        if swap in words:
            found_values.add(swap)
    #REPLACE
    count = 0
    for i in word:
        for n in surr_keys[str(i)]:
            replacement = word[:count] + n + word[count+1:]
            if replacement in words:
                found_values.add(replacement)
        count += 1
    #OUTPUT
    if len(found_values) > 0:
        status = "FOUND" 
        values = [] #get rid of cuplicates by moving all the values into a set doing a couple steps
        for i in found_values:
            values.append([with_values[i], i]) #this is for the easy sort of the list by usage
            values.sort(reverse = True) #easy sort
        final_values = []
        for i in values:
            final_values.append(i[1])
        num_found = len(found_values)
        found_spacing = 3 - len(str(num_found))
        print(" "*spacing + str(word) + " -> " + status + " "*found_spacing + str(num_found) + ": ", *final_values[:3],)
    else:
        print(" "*spacing, word, " -> ", status, sep = "")
    
if __name__ == "__main__": #finally understand what the hell is this thanks to Jack
    
    dict_file = str(input("Dictionary file => ").strip()) #dictionary file name
    print(dict_file)
    in_file = str(input("Input file => ").strip())#input file name
    print(in_file)
    key_file = str(input("Keyboard file => ").strip())#keyboard file name
    print(key_file)
    
    words = get_dictionary_words(dict_file)#just the recognized words
    with_values = get_dictionary_with_values(dict_file)#a dictioanry of word:usage format
    
    keyboard = dict() #create dictionary for each letter as key and surrounding letters as values
    for line in open(key_file):
        line = line.replace("\n", "") #disaster avoided... for now my desk can take a break from abuse
        seperated = line.split(" ")
        key = str(seperated[0])
        surrounding = []
        for i in seperated[1:]:
            surrounding.append(str(i))
        keyboard[key] = surrounding
        
    for line in open (in_file): # go line by line and output the results
        line = line.strip()
        line = line.replace("\n", "") # I love notepad fucking me over
        status = "NOT FOUND"
        spacing = 15 - len(line)
        if line in words:
            status = "FOUND"
            print(" "*spacing + line + " -> " + status, sep = "")
        else:
            get_output(line, words, with_values, keyboard, spacing) 