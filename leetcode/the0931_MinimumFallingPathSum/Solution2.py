class Solution(object):
    def minFallingPathSum(self, mx):
        rc = len(mx)

        dp = [mx[0][i] for i in range(rc)]
        dp2 = [0] * rc

        for r in range(1, rc):
            for c in range(0, rc):
                dp2[c] = float('inf')
                if c - 1 > -1:
                    dp2[c] = mx[r][c] + dp[c - 1]

                dp2[c] = min(dp2[c], mx[r][c] + dp[c])

                if c + 1 < rc:
                    dp2[c] = min(dp2[c], mx[r][c] + dp[c + 1])

            dp, dp2 = dp2, dp

        return min(dp)
