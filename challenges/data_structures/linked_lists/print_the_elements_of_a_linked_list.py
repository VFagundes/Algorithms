#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
from singly_linked_list import SinglyLinkedList


def printLinkedList(head):
    if not head.head:
        return

    node = head.head
    while node:
        print node.data
        node = node.next


data = '''2
16
13
'''

arr = data.strip().split('\n')[1:]
linked_list = SinglyLinkedList()

map(lambda x: linked_list.insert_node(int(x)), arr)

print arr

printLinkedList(linked_list)
