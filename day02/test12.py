a,b,c=eval(raw_input("shurusangeshu:"))
t = 0
if a > b:
    t = a
    a = b
    b = t
if b > c:
    t = b
    b = c
    c = t
if a > b:
    t = a
    a = b
    b = t
print (a,b,c)
