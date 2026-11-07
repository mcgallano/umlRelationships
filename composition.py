class Room:
    def __init__(self, name: str):
        self.name = name


class House:
    def __init__(self):
        # The House creates and strictly owns these Room objects
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


if __name__ == "__main__":
    my_house = House()
    for room in my_house.rooms:
        print(f"Room created: {room.name}")