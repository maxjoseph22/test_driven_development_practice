from lib.report_length import *

def test_report_length_test():
    result = report_length("python")
    assert result == "This string was 6 characters long."

def test_report_length_test_2():
    result = report_length("maximilian")
    assert result == "This string was 10 characters long."