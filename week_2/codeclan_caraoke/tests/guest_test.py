import unittest

from classes.guest import *
from classes.room import *
from classes.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 50, "Barbie Girl")
        self.guest_2 = Guest("Stuart", 100, "Crazy Train")
        self.guest_3 = Guest("Kris", 25,"War Pigs")
        self.guest_4 = Guest("Keith", 70, "3 Little Birds")
        self.guest_5 = Guest("Morag", 80, "Losing My Religion"),
        self.guest_6 = Guest("Eric", 0, "Edge of Seventeen")

        self.song_1 = Song("Hey Ya")
        self.song_2 = Song("It's Raining Men")
        self.song_3 = Song("War Pigs")
        self.song_4 = Song("Barbie Girl")
        self.song_5 = Song("3 Little Birds")

        self.room_1 = Room("Python Pop",["Barbie Girl"],[self.guest_1],3,20)
        self.room_2 = Room("HTML Heavy Metal",["War Pigs"],[self.guest_3],8,30)
        self.room_3 = Room("Ruby Reggae",["3 Little Birds"],[self.guest_5],12,40)


    
    def test_guest_has_money_in_wallet(self):
        self.assertEqual(50,self.guest_1.money)

    def test_guest_no_money_in_wallet(self):
        self.assertEqual(0,self.guest_6.money)

    # def test_split_the_cost(self):
    #     self.room_2.add_guest(self.guest_4)
    #     self.room_2.add_guest(self.guest_5)
    #     self.assertEqual(10,self.room_2)

    # def test_enough_money_for_room(self):
    #     self.assertEqual(True, self.guest_2.enough_money(self.room_2.cost))
    
    
    # def test_not_enough_money_for_room(self):
    #     self.assertEqual(False, self.guest_6.enough_money(self.room_2.cost))


    # def test_guests_favourite_song_is_available(self):
    #     self.assertEqual("Yes! What a banger!",self.room_2.songs[0])


    
