import unittest

from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 50, "Barbie Girl")
        self.guest_2 = Guest("Stuart", 100, "Crazy Train")
        self.guest_3 = Guest("Kris", 25,"War Pigs")
        self.guest_4 = Guest("Keith", 70, "3 Little Birds")
        self.guest_5 = Guest("Morag", 80, "Losing My Religion")

        self.song_1 = Song("Hey Ya")
        self.song_2 = Song("It's Raining Men")
        self.song_3 = Song("War Pigs")
        self.song_4 = Song("Barbie Girl")
        self.song_5 = Song("3 Little Birds")

        self.room_1 = Room("Python Pop",["Barbie Girl"],[self.guest_1],3,20)
        self.room_2 = Room("HTML Heavy Metal",["War Pigs"],[self.guest_3],8,30)
        self.room_3 = Room("Ruby Reggae",["3 Little Birds"],[self.guest_5],12,40)
       

    def test_check_room_name(self):
        self.assertEqual("Python Pop",self.room_1.name)
    
    def test_check_song_in_room(self):
        self.assertEqual(["Barbie Girl"], self.room_1.songs)

    def test_check_number_of_guests_in_room(self):
        self.assertEqual(1, len(self.room_1.guests))

    def test_number_of_guests_add_guest(self):
        self.room_1.add_guest(self.guest_2)
        self.assertEqual(2,len(self.room_1.guests))

    def test_number_of_guests_remove_guest(self):
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0,len(self.room_1.guests))

    
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

    # def test_split_the_cost(self):
    #     self.room_2.add_guest(self.guest_4)
    #     self.room_2.add_guest(self.guest_5)
    #     self.room_2.split_the_cost
    #     self.assertEqual(10,(self.room_2.split_the_cost))

    def test_check_guest_favourite_song(self):
        self.assertEqual("War Pigs", self.guest_3.favourite_song)

    def test_is_favourite_song_in_playlist__True(self):
        self.assertEqual("Yes! What a banger!",(self.room_2.favourite_song_in_playlist(self.room_2.songs,self.guest_3.favourite_song)))

    def test_is_favourite_song_in_playlist__False(self):
        self.assertEqual("My Ears Are Bleeding!!!",(self.room_3.favourite_song_in_playlist(self.room_3.songs,self.guest_5.favourite_song)))


