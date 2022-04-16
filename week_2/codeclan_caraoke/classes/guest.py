class Guest:
    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song


    def enough_money(self,room):
        return self.money >= room

    def pay_for_room(self,ammount):
        self.money -= ammount
