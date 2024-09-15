class BeeElephant:

    def __init__(self, bee: int, elephant: int):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal: str, value: int):
        if meal == "nectar":
            self.elephant = self.elephant - value if self.elephant - value > 0 else 0
            self.bee = self.bee + value if self.bee + value < 100 else 100
        elif meal == "grass":
            self.bee = self.bee - value if self.bee - value > 0 else 0
            self.elephant = self.elephant + value if self.elephant + value < 100 else 100
        else:
            print("Переданное meal не верно!! Передайте или nectar или grass")

    def get_value_beeelephant(self):
        return self.bee, self.elephant


be = BeeElephant(13, 87)
print(be.fly())
print(be.trumpet())
be.eat("grass", 12)
print(be.get_value_beeelephant())