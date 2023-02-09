def taxRate(income):
    if income > 250000 and income <= 400000:
        taxDeduction = income * 0.15
    elif income > 400000 and income <= 800000:
        taxDeduction = income * 0.2 + 22500
    elif income > 800000 and income <= 2000000:
        taxDeduction = income * 0.25 + 102500
    elif income > 2000000 and income <= 8000000:
        taxDeduction = income * 0.3 + 402500
    elif income > 8000000:
        taxDeduction = income * 0.35 + 2202500
    else:
        taxDeduction = 0
    return taxDeduction

annualIncome = float(input("Enter your annual income: "))
print()
if taxRate(annualIncome) == 0:
    print("You have no tax deduction")
else:
    print("Your tax deduction is: Php {}".format(taxRate(annualIncome)))

actualIncome = annualIncome - taxRate(annualIncome)
print("Your final income is {}".format(actualIncome))
input("Press enter to continue...")
