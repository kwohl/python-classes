import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Katie Wohl"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
        self.name = ""

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name

    def building_summary(self):
        print(f"{self.name} was purchased by {self.owner} on {self.date_constructed.strftime('%B %d, %Y')} and has {self.stories} stories.")



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

