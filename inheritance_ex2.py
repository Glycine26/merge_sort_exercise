#We can use all the attributes of the parent class in sub class.
#In a company, you have different types of employees: full-time employees, part-time employees, and interns. 
# All of them share some common characteristics (like having a name and an ID), 
# but they also have unique features. 
# For example, full-time employees might have benefits, part-time employees might have flexible hours, and interns might have a mentor assigned to them.

class Employee(object):
    def __init__(self, name:str, employee_id:int):
        self.name = name
        self.employee_id = employee_id

    def get_details(self,benefits):
        self.benefits = benefits
        msg1 = f"Name: {self.name}, Employee_ID: {self.employee_id}, Benefit: {benefits}"
        return msg1
    
    def get_depatrment(self,department):
        self.department = department
        msg2 = f"Name: {self.name}, Employee_ID: {self.employee_id}, Department: {department}"
        return msg2


class FullTimeEmployee(Employee):
    def __init__(self, name:str, employee_id:int):
        super().__init__(name, employee_id)
    
    def get_details(self, benefits):
        return super().get_details(benefits)
    

class Intern(Employee):
    def __init__(self, name:str, employee_id:int):
        super().__init__(name, employee_id)

    def get_depatrment(self, department):
        return super().get_depatrment(department)
        

permanent_employee = Employee("Dheeraj",26001)
print(permanent_employee.get_details("Paid Leave"))
intern_employee = Employee("Shruti",2341)
print(intern_employee.get_depatrment("Marketing"))
