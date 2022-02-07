import pytest

from linked_list import LinkedList

def intersection(ll1: LinkedList, ll2: LinkedList):
    if (ll1.tail != ll2.tail):
        return None

    len1 = len(ll1)
    len2 = len(ll2)
    
    shorter = ll1.head if len1 < len2 else ll2.head
    longer = ll2.head if len1 < len2 else ll1.head
    
    # advance longer until equal to shorter
    len_diff = abs(len1 - len2)
    for _ in range(len_diff):
        longer.next
        
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return shorter