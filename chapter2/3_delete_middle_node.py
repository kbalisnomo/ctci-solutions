import pytest

from linked_list import LinkedList, LinkedListNode

def delete_middle_node(node: LinkedListNode):
    node.value = node.next.value
    node.next = node.next.next

class Test():
    def test_delete_middle_node(self):
        node = LinkedListNode('c')
        ll = LinkedList()
        ll.add_multiple(['a', 'b', 'c', 'd'])
        expected = LinkedList()
        expected.add_multiple(['a', 'b', 'd'])
        delete_middle_node(ll.head.next.next)
        assert ll.values() == expected.values()