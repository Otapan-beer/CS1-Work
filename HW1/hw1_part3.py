character = input("Enter frame character ==> ")
print(character)

print()

height = input("Height of box ==> ")
len1 = len(height)
print(height)
height = int(height)

print()

width = input("Width of box ==> ")
len2 = len(width)
print(width)
width = int(width)

print()
print()

#Trying not to discombobulate Einstein's whole theorem and avoiding output like this: ('#', '         ', '#', '\n', '#', '         ', '#', '\n', '#', '         ', '#', '\n', '#', '         ', '#', '\n', '#', '         ', '#', '\n', '#', '         ', '#', '\n')
lenght = (len1 + len2)
ysides = (character*width)
innerWidth = (width - 2)
Left = int((innerWidth - lenght - 1)/2)
Right = int(innerWidth - lenght - Left - 1)
upperPart = ((height - 5)//2)
lowerPart = int((height - 4)/2)
filler = (height - 4 - upperPart - lowerPart)

print("Box:")
print(ysides)
print((character + " "*innerWidth + character + "\n")*upperPart,(character + " "*innerWidth + character)*filler, sep = "")
print(character, " "*Left, width, "x", height, " "*Right, character, sep = "")
print((character + " "*innerWidth + character + "\n")*lowerPart,(character + " "*innerWidth + character)*filler, sep = "")
print(ysides)
