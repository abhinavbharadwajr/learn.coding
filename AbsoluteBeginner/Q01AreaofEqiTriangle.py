import math

sqroot = math.sqrt(3)
constant = sqroot/4
sideofTriangle = int(input())

areaofTriangle = constant*(sideofTriangle*sideofTriangle)

print(round(areaofTriangle, 2))