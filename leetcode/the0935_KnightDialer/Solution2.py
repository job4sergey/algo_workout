class Solution(object):
    def knightDialer(self, N):
        MD = 10 ** 9 + 7

        deps = [(4, 6), (8, 6), (7, 9), (4, 8), (3, 9, 0), [], (1, 7, 0), (2, 6), (1, 3), (2, 4)]

        dp = [1] * 10
        dp2 = [0] * 10

        for _ in range(N - 1):
            for v in range(10):
                dp2[v] = 0
                for u in deps[v]:
                    dp2[v] = (dp2[v] + dp[u]) % MD
            dp, dp2 = dp2, dp

        res = 0
        for sm in dp:
            res = (res + sm) % MD
        return res
