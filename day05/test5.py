import math
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        print(x)
    def gety(self):
        y = (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        print(y)
x1,y1,x2,y2=eval(raw_input("Enter the endpoints of the first line segment:"))
x3,y3,x4,y4=eval(raw_input("Enter the endpoints of the second line segment:"))
a = y1 - y2
b = x2 - x1
e = x2*y1-x1*y2
c = y3 - y4
d = x4 - x3
f = x4*y3-x3*y4
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()


