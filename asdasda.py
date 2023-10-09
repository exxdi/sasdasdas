class IceCream:
    def __init__(self):
        self.flavors = []

    def add_flavor(self, flavor):
        if (self.flavors) < 3:
            self.flavors.append(flavor)
        else:
            print("You can't choose more than 3 flavors")
    def get_ice_cream(self):
        if (self.flavors) < 2:
            return "Choose more than 2 flavors"
        elif (self.flavors) <= 3:
            return f"Your Ice Cream: {', '.join(self.flavors)}"
print("Your Ice Cream:")
myicecream = IceCream()
myicecream.add_flavor(input(""))
myicecream.add_flavor(input(""))
myicecream.add_flavor(input(""))

readyicecream = myicecream.get_ice_cream()
print(readyicecream)