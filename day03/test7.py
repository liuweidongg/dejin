n = 50000.0
s = 0
a = 0
while n<=50000.0 and n>=2:
    a = (1/n)+(1/(n-1))
    s = a+s
    n = n-1
print(s)
