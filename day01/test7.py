jine = eval(raw_input("Enter the monthly saving amount:"))
s=0
for i in range (1,7):
    jine =jine*(1+0.00417)
    s = s+jine
print(s)
