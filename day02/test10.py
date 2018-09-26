import random
s = eval(raw_input(">>"))
a = random.randrange(1,101)
b = random.randrange(1,101)
c = a+b
if s==c:
    print("True")
else:
    print("Flase")
