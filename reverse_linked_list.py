# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

    def reverseList(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

#the first node is always going to end up being the last node,
# and the last node should always point to None

# create a variable to temporarily hold the value of head
# while we change head to iterate thru the list