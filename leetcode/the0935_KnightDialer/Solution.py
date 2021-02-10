class Solution(object):
    def knightDialer(self, N):
        MD = 10 ** 9 + 7

        deps = {1: (8, 6), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0),
                5: [], 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4), 0: (4, 6)}

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
