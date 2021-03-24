
from enum import Enum

class AnimalType(Enum):
    CAT  = 1
    DOG  = 2

class Animal():
    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name

    def __str__(self):
        return str(self.animal_type) + ' ' + self.name
    
    def __repr__(self):
        return str(self.animal_type) + ' ' + self.name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(AnimalType.DOG, name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(AnimalType.CAT, name)

class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.priotity_queue = []

    def printme(self):
        for cat in self.cats:
            print(cat)
        for dog in self.dogs:
            print(dog)
        for order in self.priotity_queue:
            print(order)
    
    def enqueue(self, animal: Animal) -> None:
        if animal.animal_type == AnimalType.CAT:
            self.cats.append(animal)
            self.priotity_queue.append(AnimalType.CAT)
        elif animal.animal_type == AnimalType.DOG:
            self.dogs.append(animal)
            self.priotity_queue.append(AnimalType.DOG)

    def dequeue_any(self):
        if not len(self.priotity_queue):
            return None
        atype = self.priotity_queue.pop(0)
        if atype == AnimalType.DOG:
            return self.dogs.pop(0)
        if atype == AnimalType.CAT:
            return self.cats.pop(0)

    def dequeue_cat(self):
        index_cat = self.priotity_queue.index(AnimalType.CAT)
        
        if index_cat < 0:
            return None
        
        self.priotity_queue.remove(AnimalType.CAT)
        return self.cats.pop(0)
    
    def dequeue_dog(self):
        index_dog = self.priotity_queue.index(AnimalType.DOG)
        
        if index_dog < 0:
            return None
        
        self.priotity_queue.remove(AnimalType.DOG)
        return self.dogs.pop(0)

#######

cats = [Cat(str(i)) for i in range(10) ]
print(cats)

doggos = [Dog(str(i)) for i in range(10) ]
print(doggos)

shelter = AnimalShelter()

for kitten, doggo in zip(cats, doggos):
    shelter.enqueue(kitten)
    shelter.enqueue(doggo)

shelter.printme()
print('dequeing phase any')
print(shelter.dequeue_any())
print(shelter.dequeue_any())
print(shelter.dequeue_any())
print('dequeing phase cat')
print(shelter.dequeue_cat())
print(shelter.dequeue_cat())
print(shelter.dequeue_cat())
print(shelter.dequeue_cat())
print(shelter.dequeue_cat())
print('dequeing phase dog')
print(shelter.dequeue_dog())
print(shelter.dequeue_dog())
print('whats left')
shelter.printme()

