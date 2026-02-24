import pytest
from linked_lists.doubly_linked_list import DoublyLinkedList, DoublyNode

def test_double_linked_list_creation():
    node: DoublyNode = DoublyNode(10)

    assert node.value == 10
    assert node.next is None
    assert node.prev is None

    ll: DoublyLinkedList = DoublyLinkedList()
    assert ll.head is None
    assert ll.length == 0