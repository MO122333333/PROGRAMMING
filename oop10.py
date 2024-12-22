class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def get_salary(self):
        return f"{self.name}'s salary is {self.salary}."


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        return f"{self.name} is managing the {self.department} department."


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is coding in {self.programming_language}."

class Intern(Employee):
    def __init__(self, name, salary, mentor):
        super().__init__(name, salary)
        self.mentor = mentor

    def work(self):
        return f"{self.name} is learning from {self.mentor}."



    
    employee = Employee("Ali", 3000)
    manager = Manager("Sara", 8000, "IT")
    developer = Developer("Ahmed", 5000, "Python")
   

    
    print(employee.work())
    print(manager.work())
    print(developer.work())


    print(employee.get_salary())
    print(manager.get_salary())
    print(developer.get_salary())
    
