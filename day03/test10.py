for i in range(1,10001):
    s=0  
    for j in range(1,int(i/2+1)):  
        if(i%j==0):  
            s+=j  
<<<<<<< HEAD
    if(s==i):
=======
     if(s==i):
>>>>>>> 656e56b934e92321eb9ff9e772bc2221f74dcafe
        print(s)
