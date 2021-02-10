class Solution(object):
    def PredictTheWinner(self, ns):
        sz = len(ns)
        if sz < 3:
            return True

        def prefix_sum():
            pre = [0] * sz
            r = 0

            for i, n in enumerate(ns):
                r += n
                pre[i] = r

            return pre

        def range_sum(pre, i, j):
            pre_i = 0 if i < 1 else pre[i - 1]
            return pre[j] - pre_i

        def run():
            dp = [[0] * sz for _ in range(sz)]
            # dp[i][j] - best possible loot on ns[i:j] for the player who sees ns[i:j+1] game state
            pre = prefix_sum()

            for i in range(sz):
                dp[i][i] = ns[i]

            for l in range(2, sz + 1):
                for i in range(0, sz - l + 1):
                    j = l + i - 1
                    dp[i][j] = range_sum(pre, i, j) - min(dp[i + 1][j], dp[i][j - 1])
                    # dp[i][j] = max(range_sum(pre, i, j) - dp[i + 1][j], range_sum(pre, i, j) - dp[i][j - 1])

            return pre[-1] - dp[0][sz - 1] <= dp[0][sz - 1]

        return run()
