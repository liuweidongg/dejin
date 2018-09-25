shuiliang =eval(raw_input("Enter the amount of water in kilograms:"))
chuwen = eval(raw_input("Enter the initial temperature:"))
zhongwen = eval(raw_input("Enter the final temperature:"))
Q = shuiliang * (zhongwen - chuwen)*4184
print("The energy needed is :",Q)
