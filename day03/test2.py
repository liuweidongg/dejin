j = 0
for i in range(15):
    s = 10000+10000*0.05
    j = j + s
    if i==10:
        a = j
        print(a)
    if i == 11:
        b = j
        d = b-a
        print(d)
print(j-a)

