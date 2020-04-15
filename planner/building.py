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





