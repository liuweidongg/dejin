import math
a,b,c = eval(raw_input("Enter a,b,c:"))
if (b*b-4*a*c)>0:
    r1=(-1*b+math.sqrt(b*b-4*a*c))/2*a
    r2=(-1*b-math.sqrt(b*b-4*a*c))/2*a
    print("The roots are"+str(r1)+"and"+str(r2))
elif (b*b-4*a*c)==0:
    r1=(-1*b+math.sqrt(b*b-4*a*c))/2*a
    print("The root is"+str(r1))
else:
    print("The equation has no real roots")
