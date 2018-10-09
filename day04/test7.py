import math
def distance(x1,y1,x2,y2):
    s = math.sqrt((x1-x2)**2+(y1-y2)**2)
    print(s)
x1,y1,x2,y2=eval(raw_input(">>>"))
distance(x1,y1,x2,y2)
