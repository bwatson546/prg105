import employees


def main():
    print("Please enter the Employee's information.")
    e_nam = input("Name: ")
    e_num = input("Number: ")
    e_shift = input("Shift: ")
    e_pay = float(input("Pay Rate: "))

    emp = employees.ProductionWorker(e_nam, e_num, e_shift, e_pay)

    print("======================")
    print("New Employee Entered: ")
    print("======================")
    print("NAME: ", emp.get_emp_name())
    print("NUMBER: ", emp.get_emp_num())
    print("SHIFT: ", emp.get_shift())
    print("PAY RATE: ", format(emp.get_pay_rate(), ",.2f"))


main()
