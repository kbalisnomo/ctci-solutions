import pytest

from linked_list import LinkedList

def palindrome(ll: LinkedList):
    counts = {}
    current = ll.head
    # initialize a dict element for each node
    while current:
        counts[current.value] = 0
        current = current.next
    
    # count occurences of each node value
    current = ll.head
    odd_count = 0
    while current:
        counts[current.value] += 1
        if counts[current.value] % 2:
            odd_count += 1
        else:
            odd_count -= 1
        current = current.next
    # palindromes can only contain at most 1 odd count of a character
    return odd_count <= 1

class Test():
    def test_palindrome_true(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 1])
        assert palindrome(ll) is True
    def test_palindrome_false(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 3])
        assert palindrome(ll) is False