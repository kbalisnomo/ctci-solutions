import pytest

from linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    result = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    carry = 0
    while current1 or current2:
        value = 0
        if current1:
            value += current1.value
        if current2:
            value += current2.value
        value += carry
        if value >= 10:
            value -= 10
            carry = 1
        else:
            carry = 0
        result.add(value)
        current1 = current1.next
        current2 = current2.next
    return result

class Test():
    def test_sum_lists(self):
        ll1 = LinkedList()
        ll1.add_multiple([7, 1, 6])
        ll2 = LinkedList()
        ll2.add_multiple([5, 9, 2])
        expected = LinkedList()
        expected.add_multiple([2, 1 , 9])
        assert sum_lists(ll1, ll2).values() == expected.values()