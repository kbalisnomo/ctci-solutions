import pytest

def string_rotation(s1, s2):
    if len(s1) != len(s2) == 0:
        return False
    return s2 in s1 * 2

class Test():
    def test_string_rotation_true(self):
        s1 = "watterbottle"
        s2 = "erbottlewat"
        assert string_rotation(s1, s2) == True
    def test_string_rotation_false(self):
        s1 = "foo"
        s2 = "bar"
        assert string_rotation(s1, s2) == False