def ms(p):
    for i in range(2,p+1):
        for j in range(2,i+1):
            if i%j==0:
                break
        if j == i:
            print(i,2**i-1)
ms(31)
