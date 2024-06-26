class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")        


dog = Dog('willie', 6);
dog.sit()
print(f"{dog.name} is {dog.age} years old.")