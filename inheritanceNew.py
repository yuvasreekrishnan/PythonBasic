class Employee_Details:
    emp_id = 1
    employee_name = ""
    __employee_baseSalary = 50000

    def __init__(self, emp_id, employee_name):
        self.emp_id = emp_id
        self.employee_name = employee_name

    def getBaseSlary(self):
        return self.__employee_baseSalary

    
class Developer(Employee_Details):
       additional_salary = 20000

       def __init__(self, additional_salary, emp_id,employee_name ):
            self.additional_salary = additional_salary
            super().__init__(emp_id,employee_name)

       def calculateSalary(self):
            base_salary = super().getBaseSlary()
            return base_salary+ self.additional_salary


dev = Developer(30000, 10, "yuva") 

print(dev.employee_name)
print(dev.calculateSalary())