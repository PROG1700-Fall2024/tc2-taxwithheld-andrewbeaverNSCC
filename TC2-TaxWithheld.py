# Tax Withheld Calculator
"""
Student Name: Andrew Beaver
Program Title: Tax Withheld
Description:  Tech Check 2
"""
# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Display opening message
    print("Tax Withholding Calculator")

    #prompt user for their salary and dependants
    weeklySalary = float(input("\nPlease enter the full amount of your weekly salary: "))

    dependants = float(input("How many dependants do you have?: "))

    #math to get provincial tax, federal tax and dependant deduction
    provincialTax = weeklySalary * 0.06
    federalTax = weeklySalary * 0.25
    dependantDeduction = (weeklySalary * 0.02) * dependants

    #math to get the total withheld and total take home pay
    totalWithheld = provincialTax + federalTax - dependantDeduction
    totalTakeHomePay = weeklySalary - totalWithheld

    #display all taxes and deductions to the user
    print("\nProvincial Tax Withheld: ${0:.2f}".format(provincialTax))
    print("Federal Tax Whithheld: ${0:.2f}".format(federalTax))
    print("Dependant Deduction for {0:.0f} dependants: ${1:.2f}".format(dependants,dependantDeduction))

    #Display totals to user
    print("Total Withheld: ${0:.2f}".format(totalWithheld))
    print("Total Take-Home Pay: ${0:.2f}".format(totalTakeHomePay))

    # YOUR CODE ENDS HERE

main()
