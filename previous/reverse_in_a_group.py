from linked_list import *
from typing import Optional




def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # 1. Divide the linked list into groups of k
    def get_length(node: ListNode):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def reverse(start: ListNode):
        if get_length(start) < k:
            return start
        prev: ListNode = None
        current: ListNode = start
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        start = prev 
        return start
        
    arrays = []
    current = head
    tail = head
    while current:
        count = k  
        for i in range(count - 1):
            tail = tail.next
            if not tail:
                break
        if not tail:
            arrays.append(current)
            current = None
            break
        _current = tail.next
        tail.next = None
        arrays.append(current)
        current = _current
        tail = _current

    ret_node = ListNode(0)
    t = ret_node
    for a in arrays:
        t.next = reverse(a)
        while t.next:
            t = t.next
    return ret_node.next
        

numbers = [1,2,3,4,5,6,7, 8]
head: ListNode = LinkedList.create_linked_list_from_array(numbers)
LinkedList.traverse_linked_list(head)
# reversed = reverse(head)
# LinkedList.traverse_linked_list(reversed)
h = reverseKGroup(head, 0)
LinkedList.traverse_linked_list(h)