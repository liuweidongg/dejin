s = 0
z = 0
g = 0
zs = 0
fs = 0
while 1:
    i = eval(raw_input("Enter an interger,the input ends if it is 0:"))
    if i!=0:
        g=g+1
        s = s+i
    if i>0:
        zs=zs+1
    elif i<0:
        fs=fs+1
    if i ==0:
        print("zhengshu:"+str(zs))
        print("fushu:"+str(fs))
        print("ppingjunshu:"+str(s/g))
        break
