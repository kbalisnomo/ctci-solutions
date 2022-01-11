import pytest

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if set(str1) == set(str2):
        return True
    return False

class Test:
    def test_permutation_true(self):
        str1 = "abcd"
        str2 = "dcba"
        assert is_permutation(str1, str2) is True

    def test_permutation_false(self):
        str1 = "abcd"
        str2 = "efgh"
        assert is_permutation(str1, str2) is False

