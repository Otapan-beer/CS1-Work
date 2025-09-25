minutes = input("Minutes ==> ")
x = int(minutes)
print(x)

seconds = input("Seconds ==> ")
y = int(seconds)
print(y)

miles = input("Miles ==> ")
print(miles)
miles = float(miles)

TargetMiles = input("Target Miles ==> ")
print(TargetMiles, "\n")
TargetMiles = float(TargetMiles)

print("\n")

#calculating mph
secs = int((x*60) + y)
speed = (miles/(secs/3600))

#calculating secs and minutes
mm = int(60//speed)
ms = int((3600//speed)-(mm*60))

#calculating target time
h = (TargetMiles/speed)
tm = int(h*3600//60)
ts = int(h*3600-tm*60)

#The output:
print("Pace is" , mm , "minutes and", ms, "seconds per mile.")
print("Speed is {:.2f} miles per hour.".format(speed))
print("Time to run the target distance of {:.2f} miles is {:.0f} minutes and {:.0f} seconds.".format(TargetMiles, tm, ts))
