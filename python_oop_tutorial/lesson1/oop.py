# Object Orientated Programming in Python

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
   
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 22)
print(d.get_age())
d.set_age(33)
print(d.get_age())
d2 = Dog("Bill", 24)
print(d2.get_age())

