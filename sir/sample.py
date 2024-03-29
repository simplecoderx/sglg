""" sample = "hello lynn"

sample_array =['carmen', 'buena', 'vinapor']

for x in sample_array[]:
    x += 1
    if x == 'carmen':
        print(x[2])
    else:
        print("not found")

print(sample_array)
 """


""" message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299,
1.235235245 ) """


class ProgStaff:
    companyName = 'ProgrammingLab'
    def __init__(self, pSalary):
        self.salary = pSalary
    def printInfo(self):
        print( "Company name is ", ProgStaff.companyName)
        print( "Salary is ", self.salary)
peter = ProgStaff(2500)
john = ProgStaff(2500)

""" ProgStaff.companyName = 'ProgrammingSchool'
print(peter.companyName)
print(john.companyName ) """
john.printInfo()
