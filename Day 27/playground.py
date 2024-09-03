def add(*arg):
    sum1 = 0
    for n in arg:
        print(n)
        sum1 += n
    print(sum1)
    return sum(arg)


print(add(1, 2, 3, 4, 5))  # 15


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)  # 25


class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # Ensure that the key exists in the dictionary
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Chevrolet", model="Spark")

print(my_car.__dict__)
