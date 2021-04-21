# preorder traversal
class Solution(object):
    def connect(self, r0):
        q = []
        if not r0:
            return r0

        if r0.right:
            q.append((r0.right, r0))

        if r0.left:
            q.append((r0.left, r0))

        while q:
            r, p = q.pop()

            if r == p.left:
                r.next = p.right
            elif p.next:
                r.next = p.next.left

            if r.right:
                q.append((r.right, r))

            if r.left:
                q.append((r.left, r))

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
