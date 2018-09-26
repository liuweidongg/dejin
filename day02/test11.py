day = eval(raw_input("Enter today's day:>>"))
hday = eval(raw_input("Enter the number of days elapsed since today:>>"))
a=day+hday%7
b=a%7
if b==1:
    print("monday")
elif b==2:
    print("tuesday")
elif b==3:
    print("wednesday")
elif b==4:
    print("thursday")
elif b==5:
    print("friday")
elif b==6:
    print("saturday")
elif b==0:
    print("sunday")
