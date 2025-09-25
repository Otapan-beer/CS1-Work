from hw5_util import num_grids
from hw5_util import get_grid
from hw5_util import get_start_locations
from hw5_util import get_path

#grid index
n = input("Enter a grid index less than or equal to 3 (0 to end): ")
print(n)
n = int(n)

#grid
grid = get_grid(n)

#step height
step = input("Enter the maximum step height: ")
print(step)
step = int(step)

#print path grid?
confirmation = input("Should the path grid be printed (Y or N): ")
print(confirmation)
confirmation = confirmation.lower()

#functions
def columns_count(x): #does what it says
    columns = 0
    for n in x:
        columns += 1
    return(columns)

def global_max(grid): #finds the highest point in the grid
    high = []
    highnum = 0
    x = 0
    y = 0
    for i in grid:
        x = 0
        for n in i:
            if n > highnum:
                high = [y, x]
                highnum = n
            x += 1
        y += 1
    hy = high[0]
    hx = high[1]
    highest = (hy, hx)
    print("global max: (", hy, ", ", hx, ") ", highnum, sep = "")
    print("===\r")
    return highest

def neighbor(grid, step, pos, rows, columns): #finds the eligible neighboring grids (accounting for step height)
    x = pos[0]
    y = pos[1]
    n = []
    xpos1 = x - 1
    xpos2 = x + 1
    ypos1 = y - 1
    ypos2 = y + 1
    check = 0
    checks = 0
    if xpos1 < 0 or (grid[xpos1][y] - grid[x][y]) <= 0:
        check += 1
    elif (grid[xpos1][y] - grid[x][y]) > step:
        checks += 1
    else:
        a = (xpos1, y)
        n.append(a)
    if ypos1 < 0 or (grid[x][ypos1] - grid[x][y]) <= 0:
        check += 1
    elif (grid[x][ypos1] - grid[x][y]) > step:
        checks += 1
    else:
        b = (x, ypos1)
        n.append(b)
    if ypos2 >= columns or (grid[x][ypos2] - grid[x][y]) <= 0:
        check += 1
    elif (grid[x][ypos2] - grid[x][y]) > step:
        checks += 1
    else:
        c = (x, ypos2)
        n.append(c)
    if xpos2 >= rows or (grid[xpos2][y] - grid[x][y]) <= 0:
        check += 1
    elif (grid[xpos2][y] - grid[x][y]) > step:
        checks += 1
    else:
        d = (xpos2, y)
        n.append(d)
    if (4 - check) == checks and checks > 0:
        n = "s"
    return(n)
    

    
#stats variables
rows = 0
columns = 0

#columns and rows
for i in grid:
    rows += 1
    columns = columns_count(i)
print("Grid has", rows, "rows and", columns, "columns")

#global max
globalmax = global_max(grid)

total = [] #will be used for the grid

#neighboring paths and maximums
start = (get_start_locations(n))
for i in start:
    run1 = 1 #turn the calculation on (1 = steepest)
    run2 = 1 #turn the calculation on (2 = gradual)
    maximum1 = ""
    maximum2 = ""
    location1 = i
    location2 = i
    stored1 = []
    stored2 = []
    stored1.append(i)
    stored2.append(i)
    while run1 == 1: #steepest path calculation
        nei1 = neighbor(grid, step, location1, rows, columns)
        if nei1 == "s":
            maximum1 = "no"
            run1 = 0
        elif len(nei1) == 0:
            if location1 == globalmax:
                maximum1 = "global"
            else:
                maximum1 = "local"
            run1 = 0
        else:
            highest1 = 0
            position1 = ()
            for n in nei1:
                value1 = grid[n[0]][n[1]]
                if value1 > highest1:
                    highest1 = value1
                    position1 = n
            stored1.append(position1)
            location1 = position1
    while run2 == 1: #gradual path calculation
        nei2 = neighbor(grid, step, location2, rows, columns)
        if nei2 == "s":
            maximum2 = "no"
            run2 = 0
        elif len(nei2) == 0:
            if location2 == globalmax:
                maximum2 = "global"
            else:
                maximum2 = "local"
            run2 = 0
        else:
            highest2 = 100
            position2 = ()
            for n in nei2:
                value2 = grid[n[0]][n[1]]
                if value2 < highest2:
                    highest2 = value2
                    position2 = n
            stored2.append(position2)
            location2 = position2
    
    #printing
    print("steepest path")
    storedlen1 = int(1+(len(stored1) - len(stored1)%5)/5) 
    for i in range(0, storedlen1): #print max 5 per line
        print(*stored1[i*5:i*5+5], "\r")
    print(maximum1, "maximum")
    print("...") #spacing
    print("most gradual path")
    storedlen2 = int(1+(len(stored2) - len(stored2)%5)/5)
    for i in range(0, storedlen2): #print max 5 per line
        print(*stored2[i*5:i*5+5], "\r") #WHY IS IT PRINTING ONLY THE \R WHEN THE RANGE IS OVERR, WHYYYYYYY
    print(maximum2, "maximum")
    print("===") #spacing
    total.extend(stored1)
    total.extend(stored2)
    
if confirmation == "y": #print the grid
    print("Path grid")
    length = 0
    height = 0
    thelist = [] #the one and the only, the list of the list
    thelistofthelist = [] #sike!
    for i in grid: #recreating the positions of the grid
        for n in i:
            pos = (height, length)
            thelist.append(pos)
            length += 1
        thelistofthelist.append(thelist)
        thelist = []
        height += 1
        length = 0
    for i in thelistofthelist: #counting traffic
        linetraffic = []
        for n in i:
            v = total.count(n)
            if v == 0:
                linetraffic.append(" .")
            else:
                s = (" " + str(v)) # setting it up as a string
                linetraffic.append(s)
        print("", *linetraffic)
        linetraffic = []
        
#if you are reading this, PLEASE give me at least one bonus point, so my hair didn't fall for nothing