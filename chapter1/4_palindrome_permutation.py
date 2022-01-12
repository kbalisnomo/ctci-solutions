from typing import cast
import pytest

def is_palindrome_permutation(str):
    # assume english alphabet 26 chars (a-z)
    char_counts = [0 for char in range(26)]
    odd_count = 0
    for char in str:
        # check if character is a letter
        val = ord(char.lower()) - ord('a')
        if ord('a') <= val <= ord('z'):
            char_counts[val]
            if char_counts[val] % 2:
                odd_count += 1
            else:
                odd_count -= 1
    
    # palindromes can only contain at most 1 odd count of a character
    return odd_count <= 1
        

        
        
class Test():
    def test_palindrome_permutation_true(self):
        str = "Tact Coa"
        assert is_palindrome_permutation(str) is True