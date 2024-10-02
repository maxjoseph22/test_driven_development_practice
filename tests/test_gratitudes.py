from lib.gratitudes import *

def test_nothing_added():
    gratitudes = Gratitudes()
    gratitudes.add("")
    assert gratitudes.format() == "Be grateful for: "

def test_two_things_added():
    gratitudes = Gratitudes()
    gratitudes.add("beer")
    gratitudes.add("cheese")
    assert gratitudes.format() == "Be grateful for: beer, cheese"

def test_three_things_added():
    gratitudes = Gratitudes()
    gratitudes.add("beer")
    gratitudes.add("cheese")
    gratitudes.add("wine")
    assert gratitudes.format() == "Be grateful for: beer, cheese, wine"

def int_added():
    gratitudes = Gratitudes()
    gratitudes.add(3)
    assert gratitudes.format() == "Be grateful for: 3 "

def test_nine_things_added():
    gratitudes = Gratitudes()
    gratitudes.add("beer")
    gratitudes.add("cheese")
    gratitudes.add("wine")
    gratitudes.add("beer")
    gratitudes.add("cheese")
    gratitudes.add("wine")
    gratitudes.add("beer")
    gratitudes.add("cheese")
    gratitudes.add("wine")
    assert gratitudes.format() == "Be grateful for: beer, cheese, wine, beer, cheese, wine, beer, cheese, wine"


# class Gratitudes:
#     def __init__(self):
#         self.gratitudes = []

#     def add(self, gratitude):
#         self.gratitudes.append(gratitude)

#     def format(self):
#         formatted = "Be grateful for: "
#         formatted += ", ".join(self.gratitudes)
#         return formatted
