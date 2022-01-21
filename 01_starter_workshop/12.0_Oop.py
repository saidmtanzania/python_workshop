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
     class employe