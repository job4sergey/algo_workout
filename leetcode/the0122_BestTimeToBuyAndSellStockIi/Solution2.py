class Solution(object):
    def maxProfit(self, ps):
        pre = ps[0]
        mn = pre

        res = 0
        for p in ps[1:]+[-1]:
            if p < pre:
                res += max(0, pre - mn)
                mn = p

            pre = p

        return res
