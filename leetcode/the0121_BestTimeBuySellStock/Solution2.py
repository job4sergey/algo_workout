class Solution(object):
    def maxProfit(self, ps):
        mn = 10 ** 4 + 1
        mx = 0

        for p in ps:
            mx = max(mx, p - mn)
            mn = min(mn, p)

        return mx
