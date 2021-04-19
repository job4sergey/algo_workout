from collections import deque


class Solution(object):
    def countPairs(self, r0, d):
        cn = 0

        def rec(r):
            nonlocal cn

            res = deque([0] * d)
            if not r:
                return res
            if not r.left and not r.right:
                res[0] = 1
                return res

            le = rec(r.left)
            ri = rec(r.right)

            le.appendleft(0)
            le.pop()

            ri.appendleft(0)
            ri.pop()

            pre = [0] * d
            for i in range(1, d):
                pre[i] = pre[i - 1] + ri[i]

            for i in range(1, d):
                if le[i] == 0:
                    continue

                cn += le[i] * pre[d - i]

            for i in range(d):
                res[i] = le[i] + ri[i]

            return res

        rec(r0)
        return cn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
