from hw4_util import part1_get_top

password = input("Enter a password => ")
print(password)

score = 0

#length
length = len(password)
if(length < 6):
    score += 0
elif(length <= 7):
    score += 1
    print("Length: +1")
elif(length <= 10):
    score += 2
    print("Length: +2")
else: 
    score += 3
    print("Length: +3")
   
    
#case
uppercase = 0
lowercase = 0

for char in password:
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1

if(uppercase >= 2 and lowercase >= 2):
    score += 2
    print("Cases: +2")
elif(uppercase >= 1 and lowercase >= 1):
    score += 1
    print("Cases: +1")

    
    
#digits
numbers = 0

for char in password:
    if char.isdigit():
        numbers += 1
        
if(numbers >= 2):
    score += 2
    print("Digits: +2")
elif(numbers >= 1):
    score += 1
    print("Digits: +1")
    

#punctuation
punctuation1 = 0
punctuation2 = 0
p1 = ["!", "@", "#", "$"]
p2 = ["%", "^", "&", "*"]

for char in password:
    if(char == p1[0] or char == p1[1] or char == p1[2] or char == p1[3]):
        punctuation1 += 1
    if(char == p2[0] or char == p2[1] or char == p2[2] or char == p2[3]):
        punctuation2 += 1


if(punctuation1>0):
    score += 1
    print("!@#$: +1")
if(punctuation2>0):
    score += 1
    print("%^&*: +1")
    
#NY license
chars = 0
num = 0
plate = 0
for char in password:
    if char.isalpha():
        chars += 1
        if chars >=3 and num >= 4:
            plate += 1
        elif chars >=3 and num >= 1:
            chars = 1
            num = 0
    elif char.isdigit():
        num += 1
        if chars >= 3:
            if num >= 4:
                plate += 1
        else: 
            chars = 0
            num = 0
    else:
        chars = 0
        num = 0
        
if plate > 0:
    score -= 2
    print("License: -2")
    

#Common password
found = 0
common = part1_get_top()
lower = password.lower()
for i in range(len(common)):
    if lower == common[i]:
        found += 1
if found > 0:
    score -= 3
    print("Common: -3")
    

#results
level = ""
if score <= 0:
    level = "rejected"
elif score <= 2:
    level = "poor"
elif score <= 4:
    level = "fair"
elif score <= 6:
    level = "good"
else:
    level = "excellent"
print("Combined score:", score)
print("Password is", level)
