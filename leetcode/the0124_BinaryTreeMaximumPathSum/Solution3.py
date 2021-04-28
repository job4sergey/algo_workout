class Solution(object):
    def maxPathSum(self, r0):
        res = float('-inf')

        def rec(r):
            if not r:
                return 0

            nonlocal res

            l_res = max(0, rec(r.left))
            r_res = max(0, rec(r.right))

            part_max = max(l_res, r_res) + r.val
            res = max(res, l_res + r.val + r_res, part_max)
            return part_max

        rec(r0)

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
