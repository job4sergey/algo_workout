class Solution:
    def uniquePaths(self, rc: int, cc: int) -> int:
        dp = [1] * cc
        dp2 = [0] * cc

        for r in range(1, rc):
            dp2[0] = dp[0]
            for c in range(1, cc):
                dp2[c] = dp[c] + dp2[c - 1]

            dp, dp2 = dp2, dp

        return dp[cc - 1]
