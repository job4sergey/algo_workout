# O(N) with O(N) memory
class Solution(object):
    def pathSum(self, r0, t0):
        cn = 0
        dp = {}

        def rec(r, sm):
            if not r:
                return

            nonlocal cn, dp

            sm += r.val
            if sm == t0:
                cn += 1

            pre = sm - t0
            cn += dp.get(pre, 0)

            dp[sm] = dp.get(sm, 0) + 1

            rec(r.left, sm)
            rec(r.right, sm)

            dp[sm] -= 1

            # OR, remove prefix counter when it reaches 0
            # cur = dp[sm] - 1
            # if cur == 0:
            #     dp.pop(sm)
            # else:
            #     dp[sm] = cur

        rec(r0, 0)

        return cn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
