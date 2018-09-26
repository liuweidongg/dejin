import math
r = eval(raw_input("Enter the length from the center to a vertex:"))
s =2*r* math.sin(math.pi/5)
Area = round(5*s*s/(4*math.tan(math.pi/5)),2)
print(Area)

