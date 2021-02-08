class Solution(object):
    def minPathSum(self, gr):
        rc, cc = len(gr), len(gr[0])
        dp = [gr[0][0]] * cc
        for c in range(1, cc):
            dp[c] = dp[c - 1] + gr[0][c]

        dp2 = [0] * cc
        for r in range(1, rc):
            dp2[0] = dp[0] + gr[r][0]
            for c in range(1, cc):
                dp2[c] = min(dp[c], dp2[c - 1]) + gr[r][c]

            dp, dp2 = dp2, dp

        return dp[cc - 1]
