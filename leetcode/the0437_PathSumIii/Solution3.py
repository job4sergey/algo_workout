# no memoisation, O(N * N)
class Solution(object):
    def pathSum(self, r0, t0):
        cn = 0

        def rec(r, t):
            if not r:
                return 0

            t_use = t - r.val
            res = (1 if t_use == 0 else 0) + rec(r.left, t_use) + rec(r.right, t_use)
            return res

        def start_rec(r):
            nonlocal cn
            if not r:
                return
            cn += rec(r, t0)

            start_rec(r.left)
            start_rec(r.right)

        start_rec(r0)

        return cn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
