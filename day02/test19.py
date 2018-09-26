a,b,c=eval(raw_input("Enter three edges:"))
if a+b>c and a+c>b and c+b>a:
    s = a+b+c
    print(str(s))
else:
    print("this is wrong")
