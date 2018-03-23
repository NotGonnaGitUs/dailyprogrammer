loan_amount = float(input("What is the loan amount? "))
i = float(input("Interest rate? "))/100
n = int(input("Number of periods? "))
r= i/n

emi = (loan_amount *r * ((1+ r)** (n)))  /   (((1+r)**n)-1)
print ("Your EMI is "+str(round(emi,0))+"\n")

print ("Loan schedule is as follows:")
remaining = loan_amount
print ("Principal\tInterest\t EMI\t\tAmount")
for x in range(int(n)):
    periods = remaining*r
    print(round(remaining,0),"\t\t",round(periods,0),"\t\t",round(emi,0),end="\t\t")
    remaining += (periods-emi)
    print(round(remaining,0))
