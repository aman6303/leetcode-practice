# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        mylist = []

        curr = head
        while curr:
            mylist.append(curr.val)
            curr = curr.next

        if mylist == mylist[::-1]:
            return True
        return False
