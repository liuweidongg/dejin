class Account:
    def __init__(self,idd,balance,rate):
        self.__id = idd
        self.__balance = balance
        self.__rate = rate
    def getrate(self):
        lv = self._Account__rate/100/12.0
        return lv
    def draw(self,je):
        self._Account__balance = self._Account__balance-je
    def dep(self,je1):
        self._Account__balance = self._Account__balance+je1
    def get(self):
        lx = self._Account__balance*self._Account__rate/100/12.0
        return lx
    def je(self):
        je = self._Account__balance*(1+self._Account__rate/100/12.0)
        print(self._Account__id)
        print(je)
A = Account(1122,20000,4.5)
A.getrate()
A.draw(2500)
A.dep(3000)
A.get()
A.je()
print(A.getrate())
print(A.get())


