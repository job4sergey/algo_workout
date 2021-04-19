class Solution(object):
    def rob(self, r0):
        def rec(r):
            if not r:
                return 0, 0
            use_l, not_use_l = rec(r.left)
            use_r, not_use_r = rec(r.right)

            return r.val + not_use_l + not_use_r, \
                   max(use_l, not_use_l) + max(use_r, not_use_r)

        return max(rec(r0))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
