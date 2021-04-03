# Inheritance in Python

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"I don't know what to say.")
        
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am {self.color}")
        
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "Calico")
c.show()
c.speak()

d = Dog("Jill", 25)
d.show()
d.speak()

f = Fish("Bob", 13)
f.show()
f.speak()
