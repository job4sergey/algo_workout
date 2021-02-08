from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0303_RangeSumQueryImmutable.Solution import NumArray


class Test(TestCaseBase):
    def atest(self, nums, i, j, e):
        ar = NumArray(nums)
        self.assertEquals(ar.sumRange(i, j), e)

    def test(self):
        atest = self.atest

        atest([-2, 0, 3, -5, 2, -1], 0, 0, -2)
        atest([-2, 0, 3, -5, 2, -1], 0, 2, 1)
        atest([-2, 0, 3, -5, 2, -1], 2, 5, -1)
        atest([-2, 0, 3, -5, 2, -1], 0, 5, -3)
