from __future__ import print_function
s = 0
for i in range(100,1001):
    if i%5==0 and i%6==0:
        s =s+1
        print(str(i)+"\t",end="")
        if s %10==0:
            print("")
