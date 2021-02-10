from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0486_PredictTheWinner.Solution3 import Solution


class Test(TestCaseBase):
    def atest(self, nums, e):
        so = Solution()
        self.assertEquals(so.PredictTheWinner(nums), e)

    def test(self):
        atest = self.atest

        atest([1, 5, 233, 7], True)
        atest([1, 5, 2], False)
        atest([1, 1, 1], True)
