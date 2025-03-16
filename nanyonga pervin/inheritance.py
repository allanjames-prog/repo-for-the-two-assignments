# Managing Director`s salary

class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position


    def departments(self,department):
        self.department = department
        print(f"\n {self.name} is the {self.department} department")

    
    # Manager`s  roles
class Management(Employee):

    def role(self):
        print(" -----MANAGER ROLES------: ")
        count = 1
        for roles in ("Setting goals" , "Assigning work"):
            print(count, roles)
            count += 1
        print("\n")
        

   # Manager`s salary     

class Manager_salary(Management):

    def salary(self,payment):
        self.payment = payment
        print(f" \n Manager`s salary is Shs. {self.payment}")


    # Manager`s net pay after taxes
class Net_pay(Manager_salary):

    # Imposed taxes 
    def imposed(self,taxes):
        self.taxes = taxes

        print(f"Total taxes imposed on a manager`s salary is {self.taxes}%")

    # Taxing  manager`S  salary
    def calc(self):

        answer = self.payment * self.taxes
        return  f"The tax imposed is Shs.{answer}"
    
    # Manager`s net pay after taxes
    def total(self):
        
        answer1 = self.payment - self.payment * self.taxes
        return f"Manager`s netpay is  Shs.{answer1}"
       
        

mike = Net_pay("Mrs. Orban", "Manager")
mike.departments("Management")
mike.role()
mike.salary(570000)
mike.imposed(0.02)
print(mike.calc())
print(mike.total())