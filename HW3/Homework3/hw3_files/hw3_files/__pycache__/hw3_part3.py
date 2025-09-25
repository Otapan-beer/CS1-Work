import math

bears = int(input("Number of bears => "))
print(bears)
berries = float(input("Size of berry area => "))
berries = int(berries)
print(berries)


def find_next (bears, berries, tourists):
    bears_next = int(berries/(50*(bears+1)) + bears*0.60- (math.log(1+tourists,10)*0.1))
    berries_next = (berries*1.5)- (bears+1)*(berries/14)-(math.log(1+tourists,10)*0.05)
    if(bears_next < 0):
        bears_next = 0
    if(berries_next < 0):
        berries_next = 0
    x = (bears_next, berries_next)
    return x

def tourists_next(bears):
    bears = int(bears)
    if(bears<4 or bears>15):
        tourists = 0
    elif(bears<11):
        tourists = int(bears*10000)
    else:
        bears = bears-10
        tourists = int((bears*20000)+100000)
    if(tourists < 0):
        tourists = 0
        return tourists
    else:
        tourists = int(tourists)
        return tourists

print("Year      Bears     Berry     Tourists  ")

tourists = tourists_next(bears)
lbears = []
lberries = []
ltourists = []


for i in range(0, 10):
    x = bears
    y = berries
    z = tourists
    lbears.append(x)
    lberries.append(y)
    ltourists.append(z)
    years = i+1
    year = str(years)
    yearsl = len(year)
    xs = str(x)
    ybullshit = round(y, 1)
    yvariable = ybullshit*1.0
    ys = str(round(yvariable,1))
    zs = str(z)
    xl = len(xs)
    yl = len(ys)
    zl = len(zs)
    yearsspace = 10-yearsl
    xspace = 10-xl
    yspace = 10-yl
    zspace = 10-zl
    yrounded = y*1.0
    yrounded = round(yrounded, 1)
    print(years, " "*int(yearsspace), x, " "*int(xspace), yrounded, " "*int(yspace), z, " "*int(zspace), sep = '')
    new = find_next(x, y, z)
    bears = new[0]
    berries = new[1]
    tourists = tourists_next(bears)

print()


mbears = min(lbears)
smbears = str(mbears)
mbearslen = 10 - len(smbears)

mberries = min(lberries)
mberriesvariable = (mberries * 1.0)
mberriesvariable = round(mberriesvariable, 1)
smberries = str(mberriesvariable)
mberrieslen = 10 - len(smberries)

mtourists = min(ltourists)
smtourists = str(mtourists)
mtouristslen = 10 -len(smtourists)

maxbears = max(lbears)
smaxbears = str(maxbears)
maxbearslen = 10 -len(smaxbears)

maxberries = max(lberries)
maxberriesvariable = (maxberries * 1.0)
maxberriesvariable = round(maxberriesvariable, 1)
smaxberries = str(maxberriesvariable)
maxberrieslen = 10 - len(smaxberries)

maxtourists = max(ltourists)
smaxtourists = str(maxtourists)
maxtouristslen = 10 - len(smaxtourists)

print("Min:      ",mbears, " "*mbearslen, mberriesvariable, " "*mberrieslen, mtourists, " "*mtouristslen, sep = "")
print("Max:      ", maxbears, " "*maxbearslen, maxberriesvariable, " "*maxberrieslen, maxtourists, " "*maxtouristslen, sep = "")
