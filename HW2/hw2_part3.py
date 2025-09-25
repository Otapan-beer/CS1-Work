sentence = input("Enter a sentence => ")
print(sentence)

lower = sentence.lower()

def number_happy(sentence):
    laugh = sentence.count("laugh")
    happiness = sentence.count("happiness")
    love = sentence.count("love")
    excellent = sentence.count("excellent")
    good = sentence.count("good")
    smile= sentence.count("smile")
    totalH = laugh + happiness + love + excellent + good + smile
    return(totalH)

def number_sad(sentence):
    bad = sentence.count("bad")
    sad = sentence.count("sad")
    terrible = sentence.count("terrible")
    horrible = sentence.count("horrible")
    problem = sentence.count("problem")
    hate = sentence.count("hate")
    totalS = bad + sad + terrible + horrible + problem + hate
    return(totalS)

happy = number_happy(lower)
sad = number_sad(lower)

total = ""
if(happy>sad):
    total = "happy "
elif(sad>happy):
    total = "sad "
else:
    total = "neutral "

print("Sentiment: ", "+" * happy, "-" * sad, sep = "")
print("This is a ", total, "sentence.", sep = "")