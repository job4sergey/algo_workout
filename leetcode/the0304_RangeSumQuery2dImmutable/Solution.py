from typing import List


class NumMatrix:

    def __init__(self, mx: List[List[int]]):
        rc = len(mx)
        if not rc:
            return

        cc = len(mx[0])
        if not cc:
            return

        dp = [[0] * (cc + 1) for _ in range(rc + 1)]

        for r in range(1, rc + 1):
            for c in range(1, cc + 1):
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c] - dp[r - 1][c - 1] + mx[r - 1][c - 1]

        self.dp = dp

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1 += 1
        r2 += 1
        c1 += 1
        c2 += 1
        dp = self.dp

        return dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
