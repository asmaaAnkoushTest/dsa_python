import pytest
from linked_lists.doube_linked_list import DoubleLinkedList, Node

def test_double_linked_list_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None
    assert node.prev is None

    ll: DoubleLinkedList = DoubleLinkedList()
    assert ll.head is None
    assert ll.length == 0