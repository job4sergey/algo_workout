from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0042_TrappingRainWater.Solution2 import Solution


class Test(TestCaseBase):
    def atest(self, height, e):
        s = Solution()
        self.assertEquals(s.trap(height), e)

    def test(self):
        atest = self.atest

        atest([4, 2, 3], 1)
        atest([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
