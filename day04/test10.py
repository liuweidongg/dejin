import random
while 1:
    f = random.randint(1,6)
    s = random.randint(1,6)
    if f+s==2 | f+s==3 | f+s==12:
        print("You rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("You lose")
        break
    elif f+s==7 | f+s==11:
        print("You rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("You win")
        break
    elif f+s==4 | f+s==5 | f+s==6 | f+s==8 | f+s==9 | f+s==10:
        print("you rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("point is"+str(f+s))
        t = random.randint(1,6)
        if t == f+s:
            print("you win")
            break
        elif t == 7:
            print("you lose")
            break

