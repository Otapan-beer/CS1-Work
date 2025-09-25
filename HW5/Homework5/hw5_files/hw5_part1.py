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

#print grid?
confirm = input("Should the grid be printed (Y or N): ")
print(confirm)
confirm = confirm.lower()

#functions
def print_line(x, confirm): #spacing in line
    columns = 0
    line = []
    spaces = " "
    extra = "  "
    for n in x:
        columns += 1
        s = str(n)
        if len(s) == 1:
            temp = extra + s
            line.append(temp)
        else:
            temp = spaces + s
            line.append(temp)
    if confirm == "y":
        print("", *line)
    return(columns)

def neighbor(pos, rows, columns, check): #neighbouring positions check
    x = int(pos[0])
    y = int(pos[1])
    n = []
    xpos1 = x - 1
    xpos2 = x + 1
    ypos1 = y - 1
    ypos2 = y + 1
    if xpos1 < 0:
        a = 0
    else:
        a = (xpos1, y)
        n.append(a)
    if ypos1 < 0:
        b = 0
    else:
        b = (x, ypos1)
        n.append(b)
    if ypos2 >= columns:
        c = 0
    else:
        c = (x, ypos2)
        n.append(c)
    if xpos2 >= rows:
        d = 0
    else:
        d = (xpos2, y)
        n.append(d)
    if check == "y":
        spos = "(" + str(pos[0]) + ", " + str(pos[1]) + "):"
        print("Neighbors of", spos, *n)
    else:
        return(n)
    
def elevation(path, grid, n): #elevation
    up = 0
    down = 0
    count = 0
    pathlen = len(path)
    for i in path:
        if count + 1 == pathlen:
            break
        else:
            nextstep = path[count + 1]
            x1 = i[0]
            y1 = i[1]
            x2 = nextstep[0]
            y2 = nextstep[1]
            f = grid[x1][y1]
            t = grid[x2][y2]
            dif = t - f
            if dif < 0:
                down -= dif
            else:
                up += dif
        count += 1
    summary = (down, up)
    return(summary)
    
#stats variables
rows = 0
columns = 0

#stats and/or rows
if confirm == "y":
    print("Grid", n)
for i in grid:
    rows += 1
    columns = print_line(i, confirm)
print("Grid has", rows, "rows and", columns, "columns")

#neighboring
start = (get_start_locations(n))
for i in start:
    neighbor(i, rows, columns, "y")

#path variables
path = get_path(n)
legit = 0
pathlen = len(path)
notlegit = 0
count = 0

#path code
for i in path:
    ways = []
    if count + 1 == pathlen or notlegit >= 1:
        break
    else:
        legit = 0
        ways = neighbor(i, rows, columns, "n")
        nextstep = path[count + 1]
        lengthways = len(ways)
        for n in ways:
            if nextstep == n:
                legit += 1
            else:
                legit += 0
        if legit == 0:
            print("Path: invalid step from", i, "to", nextstep)
            notlegit += 1
            break
    count += 1
if notlegit == 0:
    print("Valid path")
    du = elevation(path, grid, n)
    print("Downward", du[0])
    print("Upward", du[1])