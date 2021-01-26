from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the1250_CheckIfItIsaGoodArray.Solution import Solution


class Test(TestCaseBase):
    def atest(self, nums, e):
        so = Solution()
        self.assertEquals(so.isGoodArray(nums), e)

    def test(self):
        atest = self.atest

        atest(nums=[12, 5, 7, 23], e=True)
        atest(nums=[29, 6, 10], e=True)
        atest(nums=[3, 6], e=False)
