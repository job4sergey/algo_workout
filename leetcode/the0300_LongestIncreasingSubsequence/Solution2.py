class Solution(object):
    def lengthOfLIS(self, ns):
        sz = len(ns)
        dp = [1] * sz

        res = 1

        for i in range(1, sz):
            for j in range(i):
                if ns[j] < ns[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

            res = max(res, dp[i])

        return res
