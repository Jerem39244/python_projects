class dog:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("woof")

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
pet = dog("Jet", 10)
animal = cat("Kit", 8)
pet.info()
pet.make_sound()
animal.info()
animal.make_sound()