from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        preval = head.val
        head = head.next

        firstcrit = None
        lastcrit = None
        mindistance = None

        d = 0
        i = 1
        while head.next:
            if (preval - head.val) * (head.val - head.next.val) < 0:
                if firstcrit is None:
                    firstcrit = i
                else:
                    lastcrit = i

                    if mindistance is None or d < mindistance:
                        mindistance = d
                d = 0

            i += 1
            d += 1
            preval = head.val
            head = head.next

        if lastcrit and firstcrit:
            return [mindistance, lastcrit - firstcrit]
        else:
            return [-1, -1]
