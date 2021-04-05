from collections import deque


class Solution(object):
    def findBottomLeftValue(self, r0):
        q = deque([r0])

        def enq(r):
            res = 0

            if r.left:
                q.append(r.left)
                res += 1

            if r.right:
                q.append(r.right)
                res += 1

            return res

        def doit():
            nc = 1
            res = None

            while nc:
                nc2 = 0
                res = q.popleft()
                nc -= 1
                nc2 += enq(res)

                while nc:
                    r = q.popleft()
                    nc2 += enq(r)
                    nc -= 1

                nc = nc2

            return res.val

        return doit()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
