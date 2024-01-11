class FarmSystem:
    def __init__(self, area):
        self.area = area
    def twofieldproductivity(self):
        return self.area / 2.0
    def threefieldproductivity(self):
        return self.area * (2/3)
farm_area = int(input("Enter the area of the farm: "))
farm_system = FarmSystem(farm_area)
twofieldproductivity = farm_system.twofieldproductivity()
threefieldproductivity = farm_system.threefieldproductivity()
print(f"Productivity area for a two-field system: {twofieldproductivity:.2f}")
print(f"Productivity area for a three-field system: {threefieldproductivity:.2f}")
