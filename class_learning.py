# https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-oop


class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def discription(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking".format(self.name)


class RussellTerier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):    
        for dog in self.dogs:
            print(dog.walk())      

        
my_dogs = [ 
    Bulldog("Tom", 6),
    RussellTerier("Fletcher", 7),
    Dog("Larry", 9)
]
my_pets = Pets(my_dogs)

print('I have {} dogs'.format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print(dog.discription())
    dog.eat()

print("""And they're all {}, of course.""".format(dog.species))

are_my_dogs_hungry = False
for dogg in my_pets.dogs:
    if dogg.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
my_pets.walk()
