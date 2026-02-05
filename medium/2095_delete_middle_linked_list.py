# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_length(head: Optional[ListNode]):
            length = 0
            curr = head
            while curr is not None:
                length += 1
                curr = curr.next

            return length

        total_len = get_length(head)

        # middle_index = total_len // 2 if total_len % 2 == 0 else (total_len // 2) + 1  wrong
        mid = total_len // 2

        # special handling the edge case
        if head is None or head.next is None:
            return None

        curr = head
        for _ in range(mid - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head


# function to convert a list into linked list
def to_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


# printing a linked list
def print_list(head):
    curr = head
    out = []
    while curr:
        out.append(curr.val)
        curr = curr.next
    print(out)


if __name__ == "__main__":
    head = to_linked_list([1, 3, 4, 7, 1, 2, 6])
    result = Solution().deleteMiddle(head)
    print_list(result)
