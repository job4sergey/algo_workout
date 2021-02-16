class Solution(object):
    @staticmethod
    def bs(a, x, i, j):
        while i <= j:
            m = i + (j - i) // 2
            if a[m] == x:
                return m
            elif a[m] < x:
                i = m + 1
            else:
                j = m - 1

        return -(i + 1)  # if i < 0 then -i - 1 is insertion point

    def lengthOfLIS(self, ns):
        dp = []
        # dp[i] - minimum y ending a sequence of length i + 1
        # it can be proved that dp[i - 1] < dp[i]

        for x in ns:
            j = self.bs(dp, x, 0, len(dp) - 1)
            if j < 0:
                ip = -j - 1
                if ip == len(dp):
                    dp.append(x)
                else:
                    dp[ip] = x
            else:
                dp[j] = x

        return len(dp)
