from syllables import find_num_syllables

line = input("Enter a paragraph => ")
print(line)
lwords = line.split()
twords = len(lwords)

def asl(sentence):
    sentences = sentence.count(".")
    word = sentence.split()
    length = len(word)
    avg = float(length/sentences)
    return avg

def phw(sentence):
    count = 0
    
    words = sentence.split()
    length= len(words)
    hardw = []
    for i in range(0, length):
        word = words[i]
        number = find_num_syllables(word)
        if (number>2):
            if(word.endswith("es")):
                count += 0
            elif(word.endswith("ed")):
                count += 0
            elif(word.count("-")>0):
                count += 0
            else:
                count += 1
                hardw.append(word)
        else:
            count += 0
    return hardw

def asyl(sentence):
    split = sentence.split()
    add = 0
    for i in range(0, len(split)):
        count = find_num_syllables(split[i])
        add += count
    total = len(split)
    asyl = float(add/total)
    return asyl


hard = phw(line)
hardcount = len(hard)
hardpercent = float((hardcount/twords)*100)
average = asl(line)*100/100
asomething = asyl(line)*100/100
grfi = 0.4*(average+hardpercent)
fkri = 206.835-1.015*average-86.4*asomething

print("Here are the hard words in this paragraph:")
print(hard)
print("Statistics: ASL:{:.2f}".format(average), " PHW:{:.2f}".format(hardpercent), "% ASYL:{:.2f}".format(asomething), sep = "")
print("Readability index (GRFI): {:.2f}".format(grfi), sep = "")
print("Readability index (FKRI): {:.2f}".format(fkri), sep = "")

