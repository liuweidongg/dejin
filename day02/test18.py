num = eval(raw_input(">>"))
a = num % 10
b = num / 10
c = b % 10
d = b /10
if (a*100+c*10+d)==(d*100+c*10+a):
    print(str(num)+"is a palindrome")
else:
    print(str(num)+"is not a palindrome")
