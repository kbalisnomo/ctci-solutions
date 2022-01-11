import pytest

def is_one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    longer = str1 if len(str1) > len(str2) else str2
    shorter = str2 if len(str1) > len(str2) else str1

    found_diff = False
    l_i = 0
    s_i = 0
    while l_i < len(longer) and s_i < len(shorter):
        if longer[l_i] != shorter[s_i]:
            if (found_diff):
                return False
            found_diff = True
            if len(longer) == len(shorter):
                s_i += 1
        else:
            s_i += 1
        l_i += 1
    return True



    

class Test:
    def test_is_one_away_insert(self):
        str1 = "pale"
        str2 = "ple"
        assert is_one_away(str1, str2) is True

    def test_is_one_away_remove(self):
        str1 = "pales"
        str2 = "pale"
        assert is_one_away(str1, str2) is True

    def test_is_one_away_replace(self):
        str1 = "pale"
        str2 = "bale"
        assert is_one_away(str1, str2) is True

    def test_is_one_away_false(self):
        str1 = "pale"
        str2 = "bake"
        assert is_one_away(str1, str2) is False