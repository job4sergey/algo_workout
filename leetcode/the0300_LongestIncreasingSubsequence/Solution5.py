class Solution(object):
    @staticmethod
    def bs(a, x, i, j):
        while i < j - 1:
            m = i + (j - i) // 2
            if a[m] < x:
                i = m
            else:
                j = m

        return j

    def lengthOfLIS(self, ns):
        dp = []
        # dp[i] - minimum y ending a sequence of length i + 1
        # it can be proved that dp[i - 1] < dp[i]

        for x in ns:
            j = self.bs(dp, x, -1, len(dp))
            # dp[j:] have value >= x
            # dp[:j] have value < x
            if j == len(dp):
                dp.append(x)
            else:
                dp[j] = x

        return len(dp)
