class Employee:
    id = 10
    employee_id = "emp01"
    base_salary = 50000

    def sampleFunction(self):
        print("This is sample function")

class Developer(Employee):
    additional_salary = 30000


    def calculateFullSalary(self):
        print("the full salary calculated")


class SeniorDeveloper(Developer):
    additional_salary_dev = 20000



class Tester(Employee):
    additional_salary_dev = 20000

employee1 = Employee()
# print(employee1.employee_id)
employee1.sampleFunction()

dev = Developer()
# print(dev.additional_salary)
# print(dev.base_salary)

tester = Tester()
# print( tester.base_salary)


seDev = SeniorDeveloper()
print(seDev.additional_salary)
print(seDev.base_salary)
print(seDev.additional_salary_dev)


class mobileInfo:
    mobile_name = "nothing"
    modelYear = "2025"
    price = 35000


class mobileInfo2:
    mobile_name = "samsung"
    modelYear_two = "2025"
    price_two = 35000

class available(mobileInfo2, mobileInfo): 
    isAvailable = "true"


status = available()
print(status.mobile_name)
   


