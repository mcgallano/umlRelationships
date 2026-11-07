class Animal:
    def __init__(self, name: str):
        self.name = name


# Dog inherits from Animal
class Dog(Animal):
    def bark(self) -> str:
        return f"{self.name} says Woof!"


if __name__ == "__main__":
    my_dog = Dog("Buddy")
    print(my_dog.bark())