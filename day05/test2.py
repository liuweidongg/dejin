import math
class RP:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getp(self):
        c = self._RP__n*self._RP__side
        print(c)
    def geta(self):
        a = (self._RP__n*self._RP__side**2)/(4*math.tan(math.pi/self._RP__n))
        print(a)
#RP().getp()
#RP().geta()
#RP(6,4).getp()
#RP(6,4).getp()
RP(10,4,5.6,7.8).geta()
RP(10,4,5.6,7.8).getp()
