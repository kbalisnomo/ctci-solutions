import pytest

from linked_list import LinkedList, LinkedListNode

def loop_detection(ll: LinkedList):
    seen = {}
    current = ll.head
    while current:
        print(seen)
        if current in seen:
            return current.value
        else:
            seen[current] = True
        current = current.next
    
    return False

class Test():
    def test_loop_detection_true(self):
        n3 = LinkedListNode(3)
        n2 = LinkedListNode(2, n3)
        n1 = LinkedListNode(1, n2)
        n3.next = n1
        ll = LinkedList()
        ll.head = n1
        assert loop_detection(ll) == 1
    def test_loop_detection_false(self):
        n3 = LinkedListNode(3)
        n2 = LinkedListNode(2, n3)
        n1 = LinkedListNode(1, n2)
        ll = LinkedList()
        ll.head = n1
        assert loop_detection(ll) is False