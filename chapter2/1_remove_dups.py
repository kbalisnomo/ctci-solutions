import pytest

from linked_list import LinkedList

def remove_dups(ll: LinkedList) -> LinkedList:
    current = ll.head
    previous = None
    seen = set()
    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

class Test():
    def test_remove_dups(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 3, 1])
        expected = LinkedList()
        expected.add_multiple([1, 2, 3])
        assert remove_dups(ll).values() == expected.values()