from lib.counter import *

def test_counter_1():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_2():
    counter = Counter()
    counter.add(12)
    result = counter.report()
    assert result == "Counted to 12 so far."   

def test_counter_initial():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

    