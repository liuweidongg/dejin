from __future__ import print_function
def getPentagoalNumber(n):
    for i in range(1,n):
        s = (i*(3*i-1))/2
        print(str(s),"\t",end="")
        if i%10==0:
            print('')
getPentagoalNumber(100)
