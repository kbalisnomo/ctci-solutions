import pytest

from linked_list import LinkedList, LinkedListNode

def kth_last(k: int, ll: LinkedList) -> LinkedListNode:
    runner = current = ll.head
    # have runner move k in front of current
    for i in range(k):
        if runner == None:
            return None
        runner = runner.next
    # have runner move to end
    while runner:
        current = current.next
        runner = runner.next
    
    return current
    


class Test():
    def test_kth_last(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 3])
        expected = LinkedListNode(2)
        assert kth_last(2, ll).value == expected.value
