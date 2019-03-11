def main():     # run yearly(), which runs monthly(), which is working
    monthly_total = monthly()
    yearly(monthly_total)    # better than everything else I tried even if I'm not sure it's what we're supposed to be doing


def monthly():  # input monthly costs
    print("Please input your payments per month.")
    loan = input("LOAN REPAY: ")
    ins = input("INSURANCE: ")
    gas = input("FUEL: ")
    fix = input("MAINTENANCE COSTS: ")
    monthly_total = float(loan) + float(ins) + float(gas) + float(fix)
    print("Your total monthly payment is: $", format(monthly_total, ",.2f"))
    return monthly_total


def yearly(cost):  # run monthly(), grabbing the monthly_total and putting it in here
    yearly_total = float(cost * 12)
    print("Your yearly automobile costs are: $", format(yearly_total, ",.2f"), "! Maybe ride a bike instead!")


main()
