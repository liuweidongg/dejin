def sumDigits(n):
    summ = 0
    cd = len(str(n))
    for i in range(1,cd+1):
        a = n % 10
        n = n //10
        summ = summ +a
    print(summ)
e = eval(raw_input(">>"))
sumDigits(e)
