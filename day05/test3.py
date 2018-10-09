class fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    def p(self):
        print(self._fan__speed,self._fan__radius,self._fan__color,self._fan__on)
fan(3,True,10,'yellow').p()
fan(2,False,5,'blue')
