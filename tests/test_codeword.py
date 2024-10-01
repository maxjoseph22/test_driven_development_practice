from lib.check_codeword import *

def test_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_codeword_2():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_codeword_3():
    result = check_codeword("water")
    assert result == "WRONG!"

def test_codeword_4():
    result = check_codeword("hors")
    assert result == "WRONG!"

    
                        