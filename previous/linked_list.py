"""
Apis for linked list
"""

from typing import Any, List


class ListNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    
    @staticmethod
    def insert_at_head(head: ListNode, val: Any) -> ListNode:
        if not head:
            return ListNode(val)
        new_node = ListNode(val)
        new_node.next = head
        return new_node

    @staticmethod
    def insert_at_end(head: ListNode, value: Any) -> ListNode:
        if not head:
            return ListNode(value)
        tmp = head
        while tmp.next:
            tmp = tmp.next
        new_node = ListNode(value)
        tmp.next = new_node
        return head

    def create_linked_list_from_array(array: List[Any]) -> ListNode:
        head: ListNode = ListNode(0)
        tmp = head
        for a in array:
            new_node = ListNode(a)
            tmp.next = new_node
            tmp = tmp.next
        return head.next
    
    def traverse_linked_list(head: ListNode):
        if not head:
            return
        tmp = head
        while tmp:
            print(tmp.val, end="->")
            tmp = tmp.next
        print("")
