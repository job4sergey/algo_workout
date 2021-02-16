import bisect


class Solution(object):
    def lengthOfLIS(self, ns):
        dp = []
        # dp[i] - minimum y ending a sequence of length i + 1
        # it can be proved that dp[i - 1] < dp[i]

        for x in ns:
            j = bisect.bisect_left(dp, x)
            # dp[j:] have value >= x
            # dp[:j] have value < x
            if j == len(dp):
                dp.append(x)
            else:
                dp[j] = x

        return len(dp)
