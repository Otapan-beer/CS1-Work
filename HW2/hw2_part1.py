import math

def find_volume_sphere(radius):
    sphere = 4./3.*math.pi*radius*radius*radius
    return(sphere)

def find_volume_cube(side):
    cube = (side*side*side)
    return(cube)

gumr = input("Enter the gum ball radius (in.) => ").strip()
print(gumr)
gumr = float(gumr)

sales = input("Enter the weekly sales => ").strip()
print(sales)
sales = float(sales)

gums = (math.ceil(sales * 1.25))
gside = (math.ceil(gums**(1./3)))
edge = (gside * gumr * 2)
total = int(gside ** 3)
extra = int(total - gums)
radius = find_volume_sphere(gumr)
space = find_volume_cube(edge)
gum1 = radius * gums
gum2 = radius * total
waste1 = space - gum1
waste2 = space - gum2
 
print()

print("The machine will need to hold ", gside, " gum balls along each edge.", sep = "")
print("The total edge lenght is ", "%.2f" % edge, " inches.", sep = "")
print("Target sales were ", gums, ", but the machine will hold ", extra, " extra gum balls.", sep = "")
print("Wasted space is ", "%.2f" % waste1, " cubic inches with the target number of gum balls,\nor ", "%.2f" % waste2, " cubic inchesif you fill up the machine.", sep = "")