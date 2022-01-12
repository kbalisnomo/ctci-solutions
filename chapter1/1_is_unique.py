import pytest

def is_unique(str):
    # assuming an ASCII character set (128 characters) 
    seen = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if seen[val]:
            return False
        seen[val] = True
    
    return True

class Test:
    def test_unique_true(self):
        data_true = "abcd"
        assert is_unique(data_true) is True
    
    def test_unique_false(self):
        data_false = "abcda"
        assert is_unique(data_false) is False
