name = raw_input("Enter employee's name:")
time = eval(raw_input("Enter number of hours worked in a work:"))
pay = eval(raw_input("Enter hourly pay rate:"))
lb = eval(raw_input("Enter federal tax withholding rate"))
zl = eval(raw_input("Enter state tax withholding rate:"))
print("Employee Name:"+name)
print("Hours Worked:"+str(time))
print("Pay Rate:"+str(pay))
p = time*pay
print("Gross Pay:"+str(p))
print("Deductions")
F = p*0.2
print("  Feseral Withholding:"+str(F))
S = p*0.09
print("  State withholding:"+str(S))
sum1 = F+S
print("  Total Deduction:"+str(sum1))
Np = p - sum1
print("Net Pay"+str(Np))
