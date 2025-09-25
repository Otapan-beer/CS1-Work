# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:41:30 2024

@author: otaka
"""
import json




class BerryField:
    def __init__(self, bfield, ab, at):
        self.bfield = bfield
        self.ab = ab
        self.at = at
        self.total = 0
        
    def total_berries(self):
        for i in self.bfield:
            x = sum(i)
            self.total += x
        print("Field has", self.total, "berries.")
        
    def grid(self):
        for bear in self.ab:
            if self.bfield[bear[0]][bear[1]] == "T":
                self.bfield[bear[0]][bear[1]] = "X" #I call this future proofing
            else:
                self.bfield[bear[0]][bear[1]] = "B"
        for tourist in self.at:
            if self.bfield[tourist[0]][tourist[1]] == "B":
                self.bfield[tourist[0]][tourist[1]] = "X"
            else:
                self.bfield[tourist[0]][tourist[1]] = "T"
        for line in self.bfield:
            print("", *line, sep = "   ")


class Bear:
    def __init__(self, ab):
        self.ab = ab

    def active_bears(self):
        print("Active Bears:")
        for i in self.ab:
            direction = i[2]
            print("Bear at (", i[0], ",", i[1], ") moving ", direction, sep = "")


class Tourist:
    def __init__(self, at, ab):
        self.at = at
        self.ab = ab
        
    def active_tourists(self):
        print("Active Tourists:")
        for i in self.at:
            check = 0 #if check is 0, we did not see a bear this round
            for n in self.ab: #basically using pythagoras theorem to check the distance from every bear
                distance = ((i[0] - n[0])**2 + (i[1] - n[1])**2)**0.5
                if distance > 4:
                    check += 1
            if check == 0:
                print("Tourist at (", i[0], ",", i[1], "), 1 turns without seeing a bear.", sep = "")
            else:
                print("Tourist at (", i[0], ",", i[1], "), 0 turns without seeing a bear.", sep = "")
        
    
class Output:
    def __init__(self, bfield, ab, at):
        self.berries = BerryField(bfield, ab, at)
        self.bears = Bear(ab)
        self.tourists = Tourist(at, ab)
        
    def results(self):
        self.berries.total_berries()
        self.berries.grid()
        print()
        self.bears.active_bears()
        print()
        self.tourists.active_tourists()
        
        

if __name__ == "__main__":
    filename = input("Enter the json file name for the simulation => ")
    print(filename)
    f = open(filename)
    data = json.loads(f.read())
    bfield = data["berry_field"]
    ab = data["active_bears"]
    """rb = data["reserve_bears"]"""
    at = data["active_tourists"]
    """rt = data["reserve_tourists"]"""
    
    print()
    
    output = Output(bfield, ab, at)
    output.results()
    
    
    """
    print(bfield)
    print(ab)
    print(rb)
    print(at)
    print(rt)
    """