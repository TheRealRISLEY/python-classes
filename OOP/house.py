class House():
    def __init__(self, type, location, owner):

        self.type = type
        self.location = location
        self.owner = owner

owner_one = House("Bungalow", "Kitengela", "Sharon")
print(owner_one.type)
print(owner_one.location)
print(owner_one.owner)

print("----------end of Owner 1-------")

owner_two = House("Penthouse", "Kilimani", "Caro")
print(owner_two.type)
print(owner_two.location)
print(owner_two.owner)