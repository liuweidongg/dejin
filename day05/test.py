'''
#ep1
class first:
    def __init__(self):
        self.shu=3
    def fuc(self):
        if self.shu%2==0:
            print self.shu
            print("yes")
        else:
            print self.shu
            print("no") 
if __name__ =='__main__':
    first().fuc()
    a = first().shu
    print(a)

#ep2
class second:
    def __init__(self):
        self.num = 10
        print("a")
    def num_2(self):
        self.num = self.num**2
        print(self.num)
    def num_3(self):
        self.num = self.num**3
        print(self.num)
if __name__ =='__main__':
    #second().num_2()
    #second().num_3()
    l=second()
    l.num_2()
    l.num_3()

#eq3
class Rectangle:
    def __init__(self,width,height):
        self.w=width
        self.h=height
    def zhouchang(self):
        c=2*(self.w+self.h)
        print c
    def acre(self):
        s=self.w * self.h
        print s
Rectangle(4,40).zhouchang()
Rectangle(4,40).acre()
'''
'''

