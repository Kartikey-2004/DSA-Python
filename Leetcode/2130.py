# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # Find maximum twin sum
        ans = 0
        first, second = head, prev

        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next
        return ans
