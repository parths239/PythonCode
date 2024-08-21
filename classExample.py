class Employee:

    # constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

# creating method to print full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# creating instance
emp_1 = Employee("Parth", "Sharma", 60000)

# calling instance values
print(emp_1.email)
print(emp_1.fullname())
