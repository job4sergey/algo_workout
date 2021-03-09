class Solution(object):
    def longestPalindromeSubseq(self, s):
        sz = len(s)
        dp = [[0] * sz for _ in range(sz)]
        for i in range(sz):
            dp[i][i] = 1

        for l in range(2, sz + 1):
            for i in range(sz - l + 1):
                j = i + l - 1

                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], (2 + dp[i + 1][j - 1]) * (s[i] == s[j]))

        return dp[0][sz - 1]
