class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = ((self._LE__e*self._LE__d)-(self._LE__b*self._LE__f))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(x)
    def gety(self):
        y = ((self._LE__a*self._LE__f)-(self._LE__e*self._LE__c))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(y)
a,b,c,d,e,f = eval(raw_input(">>"))
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()
