def year(i):
    if i%400==0 | (i%4==0 & i%100!=0):
        print(366)
    else:
        print(365)
for i in range(2010,2021):
    year(i)
