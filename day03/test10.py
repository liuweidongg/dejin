for i in range(1,10001):
    s=0  
    for j in range(1,int(i/2+1)):  
        if(i%j==0):  
            s+=j  
     if(s==i):
        print(s)
