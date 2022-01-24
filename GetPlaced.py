# create an employee
class Employee:
    # with name,age and salary attributes
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# create a company that he can get placed in.


class Company:
    # initialize a employeeList
    employeeList = []
# company name should be initialized

    def __init__(self, name):
        self.name = name
        self.employeeList = []
# create a func to Get him placed in that Company he askin' for

    def get_placed(self, employee):
        self.employeeList.append(employee)

# create a func to know the no.of emplyee got placed in a company

    def got_placed(self):
        return len(self.employeeList)

# create companies,and employee objects and get that employee a company!!


tcs = Company('TCS')
cts = Company('CTS')
emp1 = Employee('Anand', '20', '20000')
emp2 = Employee('Sanand', '21', '20001')
emp3 = Employee('Banand', '22', '20002')
emp4 = Employee('Konand', '23', '20003')

tcs.get_placed(emp1)
tcs.get_placed(emp2)
cts.get_placed(emp3)
cts.get_placed(emp4)

print(cts.got_placed())
print(tcs.got_placed())

