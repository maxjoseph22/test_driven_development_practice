from lib.greet import *

def test_greet():
    result = greet("John")
    assert result == "Hello, John!"

def test_greet_2():
    result = greet("James")
    assert result == "Hello, James!"
