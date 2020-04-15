from building import Building
from city import City

eight_hundred_eighth = Building("800 8th Street", 12)
cherry_blossom = Building("Grandma's House", 3)
stillwater = Building("1755 Stillwater Circle", 3)
springHill = Building("495 Riverfront Parkway", 6)
nss = Building("301 Plus Park Blvd", 5)

eight_hundred_eighth.purchase("Roxanne Nasraty")
eight_hundred_eighth.construct()
eight_hundred_eighth.name = "Building 808"
eight_hundred_eighth.building_summary()
print()
cherry_blossom.purchase("Rachel Wohl")
cherry_blossom.construct()
cherry_blossom.name = "Cherry Blossom"
cherry_blossom.building_summary()
print()
stillwater.purchase("Katie Wohl")
stillwater.construct()
stillwater.name = "Stillwater"
stillwater.building_summary()
print()
springHill.purchase("Dwayne Massengale")
springHill.construct()
springHill.name = "SpringHill Suites"
springHill.building_summary()
print()
nss.purchase("John Wark")
nss.construct()
nss.name = "NSS"
nss.building_summary()

print()

megalopolis = City("Megalopolis", 1995)
megalopolis.construct_building(eight_hundred_eighth)
megalopolis.construct_building(cherry_blossom)
megalopolis.construct_building(stillwater)
megalopolis.construct_building(springHill)
megalopolis.construct_building(nss)

print()

for building in megalopolis.buildings:
    print(f"{building.name} is a building in the city of {megalopolis.name}! It is located at {building.address} and was designed by {building.designer}. It is currently owned by {building.owner}")
    print()
