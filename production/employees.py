class Employee:
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_num(self):
        return self.__emp_num


class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_num, shift, pay_rate):
        Employee.__init__(self, emp_name, emp_num)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        if self.__shift == "1":
            self.__shift = "Day"
        elif self.__shift == "2":
            self.__shift = "Night"
        else:
            self.__shift = "INVALID SHIFT"
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate
