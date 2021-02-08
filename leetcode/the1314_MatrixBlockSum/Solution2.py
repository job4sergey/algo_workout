from typing import List


class Solution:
    def matrixBlockSum(self, mx: List[List[int]], K: int) -> List[List[int]]:
        rc, cc = len(mx), len(mx[0])
        dp = [[0] * cc for _ in range(rc)]
        # dp[i][j] = sum(forall (0,0) <= ii, jj <= (i,j) mx[ii][jj])
        dp[0][0] = mx[0][0]

        for r in range(1, rc):
            dp[r][0] = dp[r - 1][0] + mx[r][0]

        for c in range(1, cc):
            dp[0][c] = dp[0][c - 1] + mx[0][c]

        for r in range(1, rc):
            for c in range(1, cc):
                dp[r][c] = mx[r][c] + dp[r][c - 1] + dp[r - 1][c] - dp[r - 1][c - 1]

        res = [[0] * cc for _ in range(rc)]

        for r in range(0, rc):
            for c in range(0, cc):
                r_a, c_a = max(-1, r - K - 1), max(-1, c - K - 1)
                r_d, c_d = min(rc - 1, r + K), min(cc - 1, c + K)
                r_b, c_b = r_d, c_a
                r_c, c_c = r_a, c_d

                A = dp[r_a][c_a] if r_a > -1 and c_a > -1 else 0
                B = dp[r_b][c_b] if r_b > -1 and c_b > -1 else 0
                C = dp[r_c][c_c] if r_c > -1 and c_c > -1 else 0
                D = dp[r_d][c_d]

                res[r][c] = D - B - C + A

        return res
