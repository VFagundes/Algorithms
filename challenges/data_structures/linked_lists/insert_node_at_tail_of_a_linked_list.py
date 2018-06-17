#https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
from singly_linked_list import SinglyLinkedListNode


def insertNodeAtTail(head, data):
    temp = SinglyLinkedListNode(data)
    if not head:
        head=temp
    elif not head.next:
        head.next = temp
        return head
    else:
        insertNodeAtTail(head.next,data)
    return head