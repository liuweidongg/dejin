def displaySortedNumber(num1,num2,num3):
    if num1 > num2:
        num2,num1 = num1,num2
    elif num2 > num3:
        num3,num2 = num2,num3
    elif num1 > num2:
        num2,num1 = num1,num2
    print(num1,num2,num3)
a,b,c = eval(raw_input(">>"))
displaySortedNumber(a,b,c)
