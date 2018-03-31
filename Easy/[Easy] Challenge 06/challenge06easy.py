from decimal import *
getcontext().prec = int(input("How many decimal places do you want?"))+1
step = 1
pi = Decimal(4.0)
for d in range(3,10**7,2):
    if step==0:
        pi += Decimal(4/d)
        step = 1
    else:
        pi -= Decimal(4/d)
        step = 0

print("Leibnez runs = 10^7 )\nPi is", pi)
