
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
myanimal = Animal(3)

class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    # Getter
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name

    # Setter
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname):
        self.name = newname
    def __str__(self):
        return "animal: " +str(self.name ) +": " +str(self.age)
a = Animal(15 ,"Gunnar")
b = Animal(12 ,"Jónas")
c = Animal(25 ,"Blabla Jónsson")

a_aldur = a.get_age()
b_nafn = b.get_name()
print(a ,b ,c)
print(a_aldur ,b_nafn)
aldur = Animal.set_age(Animal ,15)
nafn = Animal.set_name(Animal ,"Gunnar")
print(Animal.__str__(a))
a.set_age(10501561)
print(a)
print("")
print("")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):

        return f"{self.make} {self.model} {self.year}"

    def set_make(self ,make):
        self.make = make
    def set_year(self ,year):
        self.year = year
    def set_model(self ,model):
        self.model = model
my_car = Car("Honda", "Civic", 2022)
mycar = Car("Toyota" ,"Corolla" ,2000)

print(my_car.get_info())  # Output: "2022 Honda Civic"
print(mycar.get_info())
model = input("Sláðu inn módel")
ar = input("Sláðu inn ár")
gerd = input("Sláðu inn gerð")
mycar2 = Car(gerd ,model ,ar)
print(mycar2.get_info(
))