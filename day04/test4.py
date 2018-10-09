from __future__ import print_function
def p(ch1,ch2,number):
    s = 0
    for i in range(ord(ch1),(ord(ch2)+1)):
        s = s + 1
        print(chr(i),"\t",end="")
        if s%number==0:
            print("")
ch1,ch2 = raw_input(">>")
number = eval(raw_input(">>"))
p(ch1,ch2,number)
