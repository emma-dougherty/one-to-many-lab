import unittest
from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 50)
        self.guest_2 = Guest("Stuart", 100)
        self.guest_3 = Guest("Kris", 25)
        self.guest_4 = Guest("Keith", 70)
        self.guest_5 = Guest("Morag", 80)

        self.room_1 = Room("Python Pop",["Barbie Girl"],[self.guest_1],3)
        self.room_2 = Room("HTML Heavy Metal",["Angel of Death", "Crazy Train","War Pigs"],[self.guest_3],8)
        self.room_3 = Room("Ruby Reggae",["3 Little Birds"],[self.guest_5],12)
       
        self.song_1 = Song("Hey Ya")
        self.song_2 = Song("It's Raining Men")


    def test_check_room_name(self):
        self.assertEqual("Python Pop",self.room_1.name)
    
    def test_check_song_in_room(self):
        self.assertEqual(["Barbie Girl"], self.room_1.songs)


    # def test_check_number_of_rooms(self):
    #     self.assertEqual(2,len(self.room.room_list))
        
    # # def test_number_of_rooms_new_room(self):
    # #     self.room.add_room(self.new_room)
    # #     self.assertEqual(3,len(self.room.room_list))
    
    # # def test_name_of_room_new_room(self):
    # #     self.assertEqual("Ruby Reggae", self.room.room_list[2])

    def test_check_number_of_guests_in_room(self):
        self.assertEqual(1, len(self.room_1.guests))

    def test_number_of_guests_add_guest(self):
        self.room_1.add_guest(self.guest_2)
        self.assertEqual(2,len(self.room_1.guests))

    def test_number_of_guests_remove_guest(self):
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0,len(self.room_1.guests))

    def test_check_songs_in_room(self):
        self.assertEqual(["Barbie Girl"],self.room_1.songs)
    
    def test_songs_list_new_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(["Barbie Girl", "Hey Ya"],self.room_1.songs)

    def test_room_has_capacity(self):
        self.assertEqual(12,self.room_3.capacity)
    
    def test_too_many_in_room(self):
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_guest(self.guest_3)
        self.room_1.add_guest(self.guest_4)
        self.assertEqual(3,len(self.room_1.guests))

    def test_guest_amount_in_wallet(self):
        self.assertEqual(50,self.guest_1.money)


    