from audioop import add


class Car:
    def __init__(self,name,model,miles,fuels,engine,door):
        self.name = name
        self.model = model
        self.miles = miles
        self.fuels = fuels
        self.engine = engine
        self.door = door
    def fuels(self,fuels):
        self.fuels = self.fuels +fuels
    def drives(self,miles):
        self.miles = self.miles+miles


car = Car("Harrier","2006","1461 m/km","Petrol","2500cc",5)

print(f"Car name:{car.name} model year:{car.model} miles {car.miles} fuels {car.fuels} engine size {car.engine} doors {car.door} ")
#delete objects and its value
del car

#INHERITANCE
class Employee:
    def __init__(self,name,age,dob,address,phone,job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.phone = phone
        self.job_description = job_description
    def get_salary(self):
        print("salary printed")
class Manager(Employee):
    def __init__(self,name,age,dob,address,phone,job_description,department,employees):
        super().__init__(name,age,dob,address,phone,job_description)
        self.department = department
        self.employees = employees
    def add_Employees(self):
        print("adding employees")
mD = Manager("Daniel Mathew",23,"21-12-1997","Dodoma","0715 091 234","Managig Director","CSE","Said salim")
print(mD.name) 
print(mD.age)
mD.get_salary()
mD.add_Employees()