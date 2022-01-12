import pytest

from linked_list import LinkedList

def partition(x: int, ll: LinkedList) -> LinkedList:
    lesser = LinkedList()
    greater = LinkedList()
    current = ll.head
    while current:
        if current.value < x:
            lesser.add(current.value)
        else:
            greater.add(current.value)
        current = current.next
    lesser.tail.next = greater.head
    return lesser

class Test():
    def test_partition(self):
        x = 5
        ll = LinkedList()
        ll.add_multiple([3, 5, 8, 5, 10, 2, 1])
        expected = LinkedList()
        expected.add_multiple([3, 2, 1, 5, 8, 5, 10])
        assert partition(x, ll).values() == expected.values()
