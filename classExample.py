class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# creating instance
emp_1 = Employee("Parth", "Sharma", 60000)
emp_2 = Employee("raj", "malhotra", 60000)

# calling instance values
print(emp_1.email)
print(emp_1.fullname())

emp_1.raise_amount = 1.06
emp_1.pay_raise()
print(emp_1.pay)

emp_2.pay_raise()
print(emp_2.pay)
