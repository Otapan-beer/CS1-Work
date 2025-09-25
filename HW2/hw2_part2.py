sentence = input("Enter a word to encode ==> ").strip()
print(sentence)

print()

check1 = str(sentence)
len0 = len(sentence)

def encrypt(word):
    word = word.replace(" a", "%4%")
    word = word.replace("he", "7!")
    word = word.replace("e", "9(*9(")
    word = word.replace("y", "*%$")
    word = word.replace("u", "@@@")
    word = word.replace("an", "-?")
    word = word.replace("th", "!@+3")
    word = word.replace("o", "7654")
    word = word.replace("9", "2")
    word = word.replace("ck", "%4")
    return(word)

def decrypt(word):
    word = word.replace("%4", "ck")
    word = word.replace("2", "9")
    word = word.replace("7654", "o")
    word = word.replace("!@+3", "th")
    word = word.replace("-?", "an")
    word = word.replace("@@@", "u")
    word = word.replace("*%$", "y")
    word = word.replace("9(*9(", "e")
    word = word.replace("7!", "he")
    word = word.replace("%4%", " a")
    return(word)

enc = encrypt(sentence)
len1 = len(enc)
lendif = abs(len1 - len0)
dec = decrypt(enc)
last = ""

if(check1 != dec):
    last = "not "
else:
    last = ""



print("Encrypted as ==> ", enc, sep = "")
print("Difference in length ==> ", lendif, sep = "")
print("Deciphered as ==> ", dec, sep = "")
print("Operation is ", last, "reversible on the string.", sep = "")
