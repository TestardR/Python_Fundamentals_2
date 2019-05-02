import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Inheritance


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


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

Employee.set_raise_amt(1.05)
print(emp_1.raise_amount)

emp_str_3 = 'John-Doe-70000'
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

dev_1 = Developer('Romain', 'Testard', 50000, 'Python')
dev_2 = Developer('Roger', 'Federer', 60000, 'JavaScript')

print(dev_1.email)
print(dev_2.email)
# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(Developer.raise_amount)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(mgr_1.email)
print(mgr_1.print_emps())

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
