'''
class Dog:

    attr1="Puppy"
    attr2="Pug"

    def fun(self):
        print("My dog name is", self.attr1)
        print("My dog name is", self.attr2)

Animal=Dog()

print(Animal.attr1)
Animal.fun()
'''

class Dog:

    def __init__(self, name):
        self.name = name

    def dog_breed1(self):
        print("My dog breed is",self.name)

    def __int__(self, name):
        self.name = name

    def dog_breed2(self):
        print("My dog breed is",self.name)

Animal = Dog('Pug')

# Animal.__init__()
Animal.dog_breed1()
Animal.dog_breed1()
