income = float(input("Enter the income: "))

if income <= 85528 :
    tax = (income * 18/100) - 556.02
else:
    tax = 14839.02 + (32/100*(income-85528))

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")