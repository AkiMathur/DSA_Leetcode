# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count+=1
        midd = (count//2)+1

        curr = head
        count = 0
        while curr:
            count+=1
            if count == midd:
                return curr
            curr = curr.next