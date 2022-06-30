class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('Diego', 'Espindola', 50000)
print(emp_1.raise_amt)

emp_2 = Employee('Test', 'Employee', 60000)

emp_1.apply_raise()
print(emp_1.pay)

