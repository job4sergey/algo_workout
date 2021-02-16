class Solution(object):
    def maximalSquare(self, M):
        rc, cc = len(M), len(M[0])

        dp = [int(M[0][c] == '1') for c in range(cc)]
        dp2 = [0] * cc
        mx = max(dp)

        for r in range(1, rc):
            dp2[0] = int(M[r][0] == '1')
            mx = max(mx, dp2[0])
            for c in range(1, cc):
                dp2[c] = (min(dp[c], dp2[c - 1], dp[c - 1]) + 1) * (M[r][c] == '1')
                mx = max(mx, dp2[c])

            dp, dp2 = dp2, dp

        return mx * mx
