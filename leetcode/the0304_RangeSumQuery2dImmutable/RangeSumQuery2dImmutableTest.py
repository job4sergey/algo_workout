from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0304_RangeSumQuery2dImmutable.Solution import NumMatrix


class Test(TestCaseBase):
    def atest(self, so: NumMatrix, q, e):
        self.assertEquals(so.sumRegion(*q), e)

    def test(self):
        atest = self.atest

        so = NumMatrix([
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ])

        atest(so, [2, 1, 4, 3], 8)
        atest(so, [1, 1, 2, 2], 11)
        atest(so, [1, 2, 2, 4], 12)
