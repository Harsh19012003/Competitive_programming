# this is code for basic inheritance
class Parent:
    x = 10

    def show(self):
        print(f"the parent x shows {self.x}")

class Child(Parent):
    pass


c = Child()

print(c.x)
c.show()


# this is code for basic polymorphism with inheritance method overriding
class Parent:
    def say(self):
        print("hello")

class Child(Parent):
    # method overriding - method say of parent class has been overridden by say of child class
    def say(self):
        print("hi")


c = Child()
c.say()
print()
print()

#----------------------------------------------------------------------------------------------------------------------


class Car:
    # _colour = "moon silver"
    def __init__(self, no_of_wheels=4, speed="average"):
        self.no_of_wheels = no_of_wheels
        self.speed = speed

    def get_no_of_wheels(self):
        print(self.no_of_wheels)

    def honk(self):
        print("hon")

    def get_speed(self):
        print(self.speed)


class Sedan(Car):
    height = "low"
    def get_height(self):
        print("low")

    def honk(self):
        print("pee")

    def get_speed(self):
        print(self.speed)


class Hatchback(Car):
    height = "high"
    def get_height(self):
        print("high")

    def honk(self):
        print("pow")

    def get_speed(self):
        print(self.speed)

class Sports(Car):
    def __init__(self, no_of_wheels=4, speed="average"):
        super().__init__(no_of_wheels, speed)
        self.speed = "way to fast"

    def get_speed(self):
        print(self.speed)

class Truck:
    pass


if __name__ == "__main__":
    c1 = Car()
    c2 = Car(8)

    c1.get_no_of_wheels()
    c2.get_no_of_wheels()

    modely = Sedan(8)
    altroz = Hatchback()
    ferrari = Sports()

    print(dir(modely))

    modely.get_height()
    altroz.get_height()

    modely.get_no_of_wheels()
    altroz.get_no_of_wheels()

    modely.honk()
    altroz.honk()
    ferrari.honk()
    
    modely.get_speed()
    altroz.get_speed()
    ferrari.get_speed()
