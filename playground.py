import math

x = 10
y = 3
ans = x/y
ans = 1.9
ans = math.isnan(ans)
print(ans)


print()


s = "asdfjkl;asdfjk;ladfjk;ladfjkl;"
print(dir(s))

print(s.__contains__("asdf"))

print(s.strip())


i = 10
print(dir(i))

print(i.to_bytes(10, "big"))

print(i.__rlshift__(4))


a = 10
b = 4

print(a&b)

print(a|b)

print()
print()



#-------------------------


# basic method overloading in python using default keyword None
def say(a=None, b=None):
    if a == None and b == None:
        print("samrtyyy")
    if a != None and b == None:
        print(a)
    if a != None and b != None:
        print(a, b)

say()
say("this")
say("is", "overloading")

print()
#-------------------------

# Multiple inheritance
class Parent:
    x = 10
    def show(self):
        print(f"the parent x shows {self.x}")

class Parentb:
    y = 20
    def view(self):
        print(f"the parent y views {self.y}")

class Child(Parent, Parentb):
    pass

c = Child()
print(c.x)
print(c.y)
c.show()
c.view()


print()
print()


class Animal:
    # Public attribute
    name = ""

    # Protected attribute
    _breed = ""

    # Private attribute
    __age = 0

    def __init__(self, name, breed, age):
        self.name = name
        self._breed = breed
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, a):
        self.__age = a

class Dog(Animal):
    # Public method
    def bark(self):
        print("Woof!")

    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)
        self._breed = "german shepheard"
        self.__age = 25

# Create a new Dog object
dog = Dog("Max", "Golden Retriever", 1)

print(dog.name)
print(dog._breed)
print(dog.get_age())
print(dog.set_age(5))
print(dog.get_age())
# print(dog.__age)
