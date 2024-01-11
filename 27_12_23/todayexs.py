class FarmSystem:
    def __init__(self, area):
        self.twofield_productivity = area / 2.0
        self.threefield_productivity = area * (2/3)
farm_area = int(input("Enter the area of the farm: "))
farm_system = FarmSystem(farm_area)

print(f"Productivity area for a two-field system: {farm_system.twofield_productivity:.2f}")
print(f"Productivity area for a three-field system: {farm_system.threefield_productivity:.2f}")
