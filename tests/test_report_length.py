from lib.report_length import *

def report_length_test():
    result = report_length("python")
    assert result == "This string was 6 characters long."

def report_length_test_2():
    result = report_length("maximilian")
    assert result == "This string was 9 characters long."