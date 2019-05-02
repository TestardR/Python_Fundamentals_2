class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Romain', 'Testard', 50000)
emp_2 = Employee('Vanessa', 'Renaud', 80000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)
