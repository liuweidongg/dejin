p = eval(raw_input(">>"))
y = eval(raw_input(">>"))
n = 0.05
while n<8.125:
    n = n+0.125
    s = p*pow((1.0+n),1)
    print(s)
    m = s/12
    print(m)
