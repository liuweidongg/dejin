import math
x1,y1 = eval(raw_input(">>"))
x2,y2 = eval(raw_input(">>"))
radius = 6371.01
a1 = math.sin(math.radians(x1))
a2 = math.sin(math.radians(x2))
a3 = math.cos(math.radians(x1))
a4 = math.cos(math.radians(x2))
a5 = math.cos(math.radians(y1)-math.radians(y2))
d = radius*math.acos(a1*a2+a3*a4*a5)
print(d)
