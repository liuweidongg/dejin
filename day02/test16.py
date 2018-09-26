import random
s = eval(raw_input(">>"))
q = random.randrange(0,3)
if s==0 and q == 2:
    print("The computer is scissor,you are paper,computer won")
if s==0 and q == 0:
    print("The computer is scissor,you are scissor too,it is a draw")
if s == 0 and q == 1:
    print("The computer is scissor,you are rock,you won")
if s == 1 and q == 0:
    print("The computer is rock,you are scissor,computer won")
if s==1 and q == 1:
    print("The computer is rock,you are rock too,it is a draw")
if s ==1 and q ==2:
    print("The computer is rock,you are paper,you won")
if s == 2 and q == 0:
    print("The computer is paper,you are scissor,you won")
if s ==2 and q == 1:
    print("The computer is paper,you are rock,computer won")
if s == 2 and q == 2:
    print("The computer is paper,you are paper,it is a draw")
