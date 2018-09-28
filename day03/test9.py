x=eval(raw_input(">>"))  
a=1  
b=2  
s=0  
for i in range(1,x+1):  
    s+=pow((-1),i+1)/(2*i-1)  
p=4*s  
print(p)   
