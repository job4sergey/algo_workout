class Solution:
    def jobScheduling(self, sts, ets, ps):
        jobs = sorted(zip(sts, ets, ps))
        sz = len(ps)

        dp = [(-1, -1)] * sz  # dp[i] - maximum profit one can get from jobs[i:]
        dp[sz - 1] = (jobs[sz - 1][0], jobs[sz - 1][2])

        for k in range(sz - 2, -1, -1):
            i, j = k, sz
            while i < j - 1:
                m = i + (j - i) // 2
                if dp[m][0] < jobs[k][1]:
                    i = m  # last i s.t. dp[m][0] < jobs[k][2]
                else:
                    j = m  # first j s.t. dp[m][0] >= jobs[k][2]

            suf = dp[j][1] if j < sz else 0
            if suf + jobs[k][2] > dp[k + 1][1]:
                dp[k] = (jobs[k][0], suf + jobs[k][2])  # we can improve
            else:
                dp[k] = dp[k + 1]  # cannot improve, just reuse suffix

        return dp[0][1]  # maximum profit
