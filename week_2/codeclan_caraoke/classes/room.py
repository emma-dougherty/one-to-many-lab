class Room:
    def __init__(self, name, songs, guests, capacity,cost):
        self.name = name
        self.songs = songs
        self.guests = guests
        self.capacity = capacity
        self.cost = cost
        # self.waiting_list = []

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def add_guest(self,guest):
        self.guests.append(guest)
        if len(self.guests)>self.capacity:
            self.guests.remove(guest)


    def add_song(self,song):
        self.songs.append(song.name)

    # def split_the_cost(self):
    #     self.cost /len(self.guests)
    #     # return share


