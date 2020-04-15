class City:

    def __init__(self, name, year_established):
        self.name = name
        self.year_established = year_established
        self.mayor = ""
        self.buildings = []

    def construct_building(self, building):
        self.buildings.append(building)

    def appoint_mayor(self, name):
        self.mayor = name