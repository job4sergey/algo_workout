from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0980_UniquePathsIii.Solution import Solution


class Test(TestCaseBase):
    def atest(self, grid, e):
        so = Solution()
        self.assertEquals(so.uniquePathsIII(grid), e)

    def test(self):
        atest = self.atest

        atest([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2)
        atest([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4)
        atest([[0, 1], [2, 0]], 0)
