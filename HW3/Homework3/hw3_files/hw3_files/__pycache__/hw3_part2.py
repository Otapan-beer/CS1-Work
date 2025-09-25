turns = int(input("How many turns? => "))
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
often = int(input("How often do we see a Pokemon (turns)? => "))
print(often)

print()

def move_pokemon(position, direction, steps):
    direction = str(direction)
    direction = direction.upper()
    x = position[0]
    y = position[1]
    if(direction == "N"):
        if((y-steps) < 0):
            y = 0
        else:
            y = y-steps
    elif(direction == "S"):
        if((y+steps) > 150):
            y = 150
        else:
            y = y+steps
    elif(direction == "E"):
        if((x+steps)>150):
            x = 150
        else:
            x = x+steps
    elif(direction == "W"):
        if((x-steps)<0):
            x = 0
        else:
            x = x-steps
    if(x>150):
        x = 150
    elif(x<0):
        x = 0
    elif(y>150):
        y=150
    elif(y<0):
        y = 0
    position = (x,y)
    return position
  
t = 0
n = 0
ratio = []
row = 75
column = 75
startpos = (row, column)

print("Starting simulation, turn", n, name, "at", startpos)
if(turns==0):
    newpos = startpos
    print(name, " ends up at ", newpos, ", Record: ", ratio, sep = "")
else:
    while(n<turns):
        if(t==1):
            direction = str(input("What direction does {} walk? => ".format(name)))
            print(direction)
            newpos = move_pokemon((row, column), direction, 5)
            row = newpos[0]
            column = newpos[1]
            n+=1
            t-=1
        elif(t==0):
            if(n>0 and (n%often) == 0):
                print("Turn ", n, ", ", name, " at ", (row, column), sep = "")
                pokemontype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
                print(pokemontype)
                pokemontype = pokemontype.upper()
                if(pokemontype == "W"):
                    newpos = move_pokemon((row, column), direction, 1)
                    print(name, "wins and moves to", newpos)
                    row = newpos[0]
                    column = newpos[1]
                    ratio.append("Win")
                elif(pokemontype == "G"):
                    newpos = move_pokemon((row, column), direction, -10)
                    print(name, "runs away to", newpos)
                    row = newpos[0]
                    column = newpos[1]
                    ratio.append("Lose")
                else:
                    ratio.append("No Pokemon")
                t+=1
            elif(n==0):
                direction = str(input("What direction does {} walk? => ".format(name)))
                print(direction)
                newpos = move_pokemon((row, column), direction, 5)
                row = newpos[0]
                column = newpos[1]
                n+=1
            elif((n%often)>0):
                direction = str(input("What direction does {} walk? => ".format(name)))
                print(direction)
                newpos = move_pokemon((row, column), direction, 5)
                row = newpos[0]
                column = newpos[1]
                n+=1
    if(n>0 and (n%often) == 0):
        print("Turn ", n, ", ", name, " at ", (row, column), sep = "")
        pokemontype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(pokemontype)
        pokemontype = pokemontype.upper()
        if(pokemontype == "W"):
            newpos = move_pokemon((row, column), direction, 1)
            print(name, "wins and moves to", newpos)
            row = newpos[0]
            column = newpos[1]
            ratio.append("Win")
        elif(pokemontype == "G"):
            newpos = move_pokemon((row, column), direction, -10)
            print(name, "runs away to", newpos)
            row = newpos[0]
            column = newpos[1]
            ratio.append("Lose")
        else:
            ratio.append("No Pokemon")
        
    print(name, " ends up at ", newpos, ", Record: ", ratio, sep = "")