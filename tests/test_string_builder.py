from lib.string_builder import *

def test_no_string_added():
    stringbuilder = StringBuilder()
    stringbuilder.add("")
    assert stringbuilder.size() == 0
    assert stringbuilder.output() == ""

def test_string_added():
    stringbuilder = StringBuilder()
    stringbuilder.add("maximilian")
    assert stringbuilder.size() == 10
    assert stringbuilder.output() == "maximilian"







    # class StringBuilder:
    # def __init__(self):
    #     self.str = ""

    # def add(self, str):
    #     self.str += str

    # def size(self):
    #     return len(self.str)

    # def output(self):
    #     return self.str
