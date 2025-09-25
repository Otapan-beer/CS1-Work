# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:06:37 2024

@author: otaka
"""


if __name__ == "__main__": #I have to appologise to my tab and enter for mashing so hard

#functions
    def parsing(file):  # parsing
        newfile = []
        for i in file:
            i = i.strip()  # Make sure to use the result of strip
            word = ""
            for n in i:
                if n.isalpha():
                    word += n.lower()
            if len(word) > 0:
                newfile.append(word)  # Corrected: use parentheses to call append
        return newfile
             
    def remove_stopwords(stopset, words):
        new = []
        for i in words:
            if i not in stopset:
                new.append(i)
        return new
            
    def get_len(l):
        letters = 0
        words = len(l)
        for i in l:
            letters += len(i)
        length = letters/words * 1.00
        return length

    def get_ratio(l):
        distinct = set()
        length = len(l)
        for i in l:
            distinct.add(i)
        words = len(distinct)
        ratio = words*1.000/length*1.000
        return ratio

    def get_len_list(l):
        copy = l.copy()
        sort = copy.sort() #idk why l=l.sort(returns None)
        lengths = []
        maxlen = 0
        for i in copy:
            length = len(i)
            if length > maxlen:
                maxlen = length
        n = 0
        while n < maxlen:
            lengths.append(set())
            n += 1
        for x in copy:
            length = len(x)
            lengths[length-1].add(x)
        return(lengths)

    def print_word_lengths(word_sets):
        copy = word_sets.copy()
        for length, words in enumerate(copy, start=1):  # Start length at 1 for list indexing
            word_count = len(words)
            words_sorted = sorted(words)  # Sort words alphabetically
            if word_count > 6:
                preview = f"{' '.join(words_sorted[:3])} ... {' '.join(words_sorted[-3:])}"
                print(f" {length:3}: {word_count:3}: {preview}")
            elif word_count == 0:
                preview = ""
                print(f" {length:3}: {word_count:3}:{preview}")
            else:
                preview = ' '.join(words_sorted)
                print(f" {length:3}: {word_count:3}: {preview}")
            
    def find_pairs(words, max_sep):
        pairs = set()  
        copy = words.copy()
        count = 0
        for i in range(1, len(copy)):
            word1 = copy[i]
            for n in range(1, max_sep + 1):
                if ((i-n) >= 0):
                    word2 = copy[i-n]
                    temp = [word1, word2]
                    temp.sort()
                    pairs.add((temp[0], temp[1]))
                    count += 1
        sort = sorted(pairs)
        total = len(sort)
        r = total/count * 1.000
        print(" ", total, "distinct pairs") #these are the prints for number 4
        if total <= 10:
            for i in sort:
                print(" ", *i)
        else:
            for i in sort[:5]:
                print(" ", *i)
            print("  ...")
            for i in sort[-5:]:
                print(" ", *i)
        print("5. Ratio of distinct word pairs to total: {:.3f}".format(r) )
        return(r) #this returns the ratio for number 5
    
    def jaccard_similarity(new1, new2): #calculate Jaccard similarity
        set1 = set()
        set2 = set()
        for i in new1:
            set1.add(i)
        for i in new2:
            set2.add(i)
        if not set1 and not set2:
            return 0
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union * 1.000 if union > 0 else 0
    
    def word_similarity(word_set1, word_set2): #calculate word similarity
        copy1 = word_set1.copy()
        copy2 = word_set2.copy()
    

    #stopfile
    stop_file = open("stop.txt", "r")
    stopwords = []
    for line in stop_file:
        stopwords.append(line.strip())
        
    #input
    file1 = input("Enter the first file to analyze and compare ==> ") # getting the first file
    print(file1)
    read1 = open(file1, "r")
    f1 = []
    for line in read1:
        line = line.strip().split(" ")
        f1.extend(line)
    file2 = input("Enter the second file to analyze and compare ==> ") # getting the second file
    print(file2)
    read2 = open(file2, "r")
    f2 = []
    for line in read2:
        line = line.strip().split()
        f2.extend(line)
    seperation = int(input("Enter the maximum separation between words in a pair ==> ")) # getting sep
    print(seperation)

    #code
    l1 = parsing(f1)
    l2 = parsing(f2)
    ls = parsing(stopwords)
    stopset = set()
    for i in ls:
        stopset.add(i)
    new1 = remove_stopwords(stopset, l1)
    new2 = remove_stopwords(stopset, l2)
    length1 = get_len(new1)
    length2 = get_len(new2)
    lenlist1 = get_len_list(new1)
    lenlist2 = get_len_list(new2)
    ratio1 = get_ratio(new1)
    ratio2 = get_ratio(new2)
    
    #first space
    print()
    
    #first print
    print("Evaluating document", file1)
    print("1. Average word length: {:.2f}".format(length1))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio1))
    print("3. Word sets for document ", file1, ":", sep = "")
    print_word_lengths(lenlist1)
    print("4. Word pairs for document", file1)
    total_pairs1 = find_pairs(new1, seperation)
    #second space
    print()
    
    #second print
    print("Evaluating document", file2)
    print("1. Average word length: {:.2f}".format(length2))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio2))
    print("3. Word sets for document ", file2, ":", sep = "")
    print_word_lengths(lenlist2)
    print("4. Word pairs for document", file2)
    total_pairs2 = find_pairs(new2, seperation)
    #space for comparison
    print()
    
    #summary comparison
    print("Summary comparison")
    if length1 > length2:
        print("1.", file1, "on average uses longer words than", file2)
    elif length1 == length2:
        print("1.", file1, "and", file2, "have the same word length")
    else:
        print("1.", file2, "on average uses longer words than", file1)
    similarity = jaccard_similarity(new1, new2)
    print("2. Overall word use similarity: {:.3f}".format(similarity))
    print("3. Word use similarity by length:")
    