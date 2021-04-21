from collections import deque


class Solution(object):
    def connect(self, r0):
        q = deque()
        if not r0:
            return r0

        cn = 0
        if r0.left:
            cn += 1
            q.append((r0.left, r0))

        if r0.right:
            cn += 1
            q.append((r0.right, r0))

        while q:
            cn2 = 0

            for _ in range(cn):
                r, p = q.popleft()

                if r == p.left:
                    r.next = p.right
                elif p.next:
                    r.next = p.next.left

                if r.left:
                    q.append((r.left, r))
                    cn2 += 1

                if r.right:
                    q.append((r.right, r))
                    cn2 += 1

            cn = cn2

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
