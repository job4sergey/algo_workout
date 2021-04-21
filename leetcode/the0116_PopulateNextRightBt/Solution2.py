class Solution(object):
    def connect(self, r0):
        def rec(r, p):
            if not r:
                return

            if p:
                if r == p.left:
                    r.next = p.right
                elif p.next:
                    r.next = p.next.left

            rec(r.left, r)
            rec(r.right, r)

        rec(r0, None)
        return r0


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
