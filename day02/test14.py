yue = eval(raw_input(">>"))
nian = eval(raw_input(">>"))
if nian%400==0 | (nian%4==0 & nian%100 != 0):
    if yue == 1:
        print(31)
    if yue == 2:
        print(29)
    if yue == 3:
        print(31)
    if yue == 4:
        print(30)
    if yue == 5:
        print(31)
    if yue == 6:
        print(30)
    if yue == 7:
        print(31)
    if yue == 8:
        print(31)
    if yue == 9:
        print(31)
    if yue == 10:
        print(31)
    if yue == 11:
        print(30)
    if yue == 12:
        print(31)
else:
    if yue == 1:
        print(31)
    if yue == 2:
        print(28)
    if yue == 3:
        print(31)
    if yue == 4:
        print(30)
    if yue == 5:
        print(31)
    if yue == 6:
        print(30)
    if yue == 7:
        print(31)
    if yue == 8:
        print(31)
    if yue == 9:
        print(30)
    if yue == 10:
        print(31)
    if yue == 11:
        print(30)
    if yue == 12:
        print(31)



