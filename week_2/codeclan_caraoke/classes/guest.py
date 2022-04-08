class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money


    def enough_money(self,room):
        return self.money >= room.cost