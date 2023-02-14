class Car():

    def __init__(self, Owner, type, colour):

        self.Owner = Owner
        self.type = type
        self.colour = colour

owner_one = Car("John", "Benz", "White")
print(owner_one.Owner)
print(owner_one.type)
print(owner_one.colour)

print("-------End of Owner 1------------")

owner_two = Car("Shadrack", "Volvo", "Black")
print(owner_two.Owner)
print(owner_two.type)
print(owner_two.colour)