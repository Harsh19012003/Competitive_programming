class Car:
    height = None
    no_of_wheels = 4
    cc_engine = None

    def get_height():
        pass


class Sedan(Car):
    height = "low"
    def get_height():
        print("low")


class Hatchback():
    height = "high"
    def get_height():
        print("high")



if __name__() == "__main__":
    c = Car
    
    modely = Sedan()
    altroz = Hatchback()


    modely.get_height()
    altroz.get_height()
