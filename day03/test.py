'''
a = 'iasdsdasda'
b= 0
c = len(a)
while b<c:
   print(a[b])
   b+=1
import random
a = random.randrange(1,3)
s = eval(raw_input(">>"))
while a-s!=0:
    if a>s:
        print("you are low")
    elif a<s:
        print("you are high")
    s = eval(raw_input(">>"))
while a-s==0:
    print("you are right")
    break
'''
#Ep2
'''
sum1 = 0
i = 0
while i < 1001:
    sum1 = i+sum1
    i+=1
print(sum1)
'''
#Ep3
'''i = 1
sum1 = 0
for sum1 in range(0,10000,sum1):
    sum1=sum1+i
    i=i+1
print(sum1)
'''
#Eq4
'''
from __future__ import print_function
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='')
    print()
'''
#Eq5
def first(num1,num2,num3):
    print(num1,num2,num3)
    return num1,num2,num3
def dier(num1,num2,num3):
    num4=num1*num1
    num5=num2*num2
    num6=num3*num3
    return num4,num5,num6
def san(num1,num2,num3,num4,num5,num6):
    n1=num4-num1
    n2=num5-num2
    n3=num6-num3
    print(n1,n2,n3)

a,b,c = first(1,2,3)
d,e,f = dier(a,b,c)
san(a,b,c,d,e,f)
