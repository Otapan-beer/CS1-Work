# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:24:39 2024

@author: otaka
"""

#I tried, I really did, rip more than 20 hours of non-stop work for 6/100, fuck me, 
#why do I have to go through every single possibility before finding the right solution too late to start over again
#PLEASE FOR THE LOVE OF GOD UPDATE THE SHITTY INSTRUCTIONS
#I AM TRYING TO DO LIKE 50 DIFFERENT THINGS AT THE SAME TIMES AND THE ERRORS JUST START LOOPING ONE ANOTHER LIKE HOW???
#WHY WHEN I FIX BUG A BUG B APPEARS, AND WHEN I FIX THAT BUG C APPEARS AND WHEN I FIX C, A COMES BACK, KILL ME
#I AM PRITING EVERYTHING OUT OVER AND OVER AGAIN TO TRY AND FIGURE IT OUT BUT NOW
#AND WHY DO THE INSTRUCTIONS SOMETIMES JUST LIE???

import json

class BerryField:
    def __init__(self, bfield, ab, at, turn):
        self.bfield = bfield
        self.ab = ab
        self.at = at
        self.turn = turn
        self.total = 0

    def total_berries(self):
        self.total = 0  # Reset total to 0 before counting
        for i in self.bfield:
            x = sum(i)
            self.total += x
        print("Field has", self.total, "berries.")
        
    def grow_berries(self): 
        for i in range(len(self.bfield)): 
            for j in range(len(self.bfield[0])): 
                if 1 <= self.bfield[i][j] < 10: 
                    self.bfield[i][j] += 1 
        for i in range(len(self.bfield)): 
            for j in range(len(self.bfield[0])): 
                if self.bfield[i][j] == 10: 
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]: 
                        ni, nj = i + di, j + dj 
                        if 0 <= ni < len(self.bfield) and 0 <= nj < len(self.bfield[0]) and self.bfield[ni][nj] == 0: 
                            self.bfield[ni][nj] = 1


        

    def grid(self):
        self.copy = [x.copy() for x in self.bfield]
        if self.turn == 0:
            count = 0
            for bear in self.ab:
                if self.copy[bear[0]][bear[1]] == "T":
                    self.copy[bear[0]][bear[1]] = "X"  # I call this future-proofing
                    self.ab[count] = [bear[0], bear[1], bear[2], 3]
                else:
                    self.copy[bear[0]][bear[1]] = "B"
                    self.ab[count] = [bear[0], bear[1], bear[2], 0]
                count += 1
            count = 0
            for tourist in self.at:
                if self.copy[tourist[0]][tourist[1]] == "B":
                    self.copy[tourist[0]][tourist[1]] = "X"
                    self.at[count] = [tourist[0], tourist[1], 4]
                else:
                    self.copy[tourist[0]][tourist[1]] = "T"
                    self.at[count] = [tourist[0], tourist[1], 0]
                count += 1
        else:
            self.grow_berries()
            DIRECTIONS = {
                "N": (-1, 0),
                "S": (1, 0),
                "E": (0, 1),
                "W": (0, -1),
                "NE": (-1, 1),
                "NW": (-1, -1),
                "SE": (1, 1),
                "SW": (1, -1),
            }
            for bearnum, bear in enumerate(self.ab):
                eaten = 0
                steps = 0
                #print(f"Starting bear {bearnum} at ({bear[0]}, {bear[1]}), Direction: {bear[2]}, Sleep: {bear[3]}")
                while eaten < 30 and bear[3] == 0 and steps < 100:
                    direction = DIRECTIONS[bear[2]]
                    #print(f"Bear {bearnum} eating at ({bear[0]}, {bear[1]})")
                    eaten += self.bfield[bear[0]][bear[1]]
                    self.bfield[bear[0]][bear[1]] = 0
                    self.copy[bear[0]][bear[1]] = 0
            
                    new_x = bear[0] + direction[0]
                    new_y = bear[1] + direction[1]
            
                    if new_x < 0 or new_x >= len(self.copy) or new_y < 0 or new_y >= len(self.copy[0]):
                        #print(f"Bear {bearnum} left the field at ({new_x}, {new_y})")
                        self.ab[bearnum] = [new_x, new_y, bear[2], 0]
                        break
            
                    if self.copy[new_x][new_y] == "T":
                        #print(f"Bear {bearnum} encountered a tourist at ({new_x}, {new_y})")
                        self.copy[new_x][new_y] = "X"
                        self.ab[bearnum] = [new_x, new_y, bear[2], 3]
                        break
            
                    if self.copy[new_x][new_y] == "X":
                        #print(f"Bear {bearnum} encountered 'X' at ({new_x}, {new_y})")
                        self.bfield[bear[0]][bear[1]] = 0
                        self.copy[bear[0]][bear[1]] = 0
                        self.ab[bearnum] = [new_x, new_y, bear[2], 0]
                        break # it is a mistake but at least it wont loop infinitely
                    
                    else: 
                        #print(f"Bear {bearnum} moved to ({new_x}, {new_y})")
                        if self.copy[new_x][new_y] != "X":
                            eaten += self.bfield[new_x][new_y]
                            self.bfield[new_x][new_y] = 0
                            self.copy[bear[0]][bear[1]] = 0
                            self.copy[new_x][new_y] = "B"
                            self.ab[bearnum] = [new_x, new_y, bear[2], 0]
                    self.ab[bearnum] = [new_x, new_y, bear[2], 0] #updating position
                    steps += 1


            for bear in self.ab:
                if (bear[0] < 0) or (bear[0] >= len(self.copy)) or (bear[1] < 0) or (bear[1] >= len(self.copy[0])):
                    print("Bear at (", bear[0], ",", bear[1], ") moving ", bear[2], " - Left the Field", sep="")
            for tourist in self.at:
                if tourist[2] == 4:
                    print("Tourist at (", tourist[0], ",", tourist[1], "), 0 turns without seeing a bear. - Left the Field", sep="")
                    self.at.remove(tourist)
                elif tourist[2] == 3:
                    print("Tourist at (", tourist[0], ",", tourist[1], "), 3 turns without seeing a bear. - Left the Field", sep="")
                    self.at.remove(tourist)
        self.total_berries()
        for line in self.copy:
            linestring = ""
            for obj in line:
                sth = str(obj)
                if len(sth) == 2:
                    linestring += "  " + str(obj)
                else:
                    linestring += "   " + str(obj)
            print(linestring)


class Bear:
    def __init__(self, ab, turn):
        self.ab = ab
        self.turn = turn

    def active_bears(self):
        print("Active Bears:")
        count = 0
        for i in self.ab:
            direction = i[2]
            if i[3] > 0 and self.turn > 0:
                print("Bear at (", i[0], ",", i[1], ") moving ", direction, "- Asleep for", i[3], "more turns", sep="")
                self.ab[count][3] -= 1
            else:
                print("Bear at (", i[0], ",", i[1], ") moving ", direction, sep="")
            count += 1


class Tourist:
    def __init__(self, at, ab, turn):
        self.at = at
        self.ab = ab
        self.turn = turn

    def active_tourists(self):
        print("Active Tourists:")
        count = 0
        for i in self.at:
            check = 0  # if check is 0, we did not see a bear this round
            for n in self.ab:  # basically using Pythagoras theorem to check the distance from every bear
                distance = ((i[0] - n[0]) ** 2 + (i[1] - n[1]) ** 2) ** 0.5
                if distance > 4:
                    check += 1
            if check == 0:
                print("Tourist at (", i[0], ",", i[1], "), ", i[2] + 1, " turns without seeing a bear.", sep="")
                self.at[count][2] += 1
            else:
                print("Tourist at (", i[0], ",", i[1], "), 0 turns without seeing a bear.", sep="")
                self.at[count][2] = 0


class Output:
    def __init__(self, bfield, ab, at, turn):
        self.berries = BerryField(bfield, ab, at, turn)
        self.bears = Bear(ab, turn)
        self.tourists = Tourist(at, ab, turn)
        self.turn = turn  # Add this line to initialize the 'turn' attribute
        
    def update(self):
        self.berries.turn += 1
        self.bears.turn += 1
        self.tourists.turn += 1

    def results(self):
        self.berries.grid()
        print()
        self.bears.active_bears()
        print()
        self.tourists.active_tourists()
        self.update()
        



if __name__ == "__main__":
    filename = input("Enter the json file name for the simulation => ")
    print(filename)
    with open(filename) as f:
        data = json.loads(f.read())
    bfield = data["berry_field"]
    ab = data["active_bears"]
    at = data["active_tourists"]

    print()
    turn = 0
    print("Starting Configuration")
    output = Output(bfield, ab, at, turn)
    output.results()
    turn += 1
    for i in range(1, 6):
        print()
        print("Turn:", i)
        output.turn = i  # Update the 'turn' attribute for each turn
        output.results()
        turn += 1
