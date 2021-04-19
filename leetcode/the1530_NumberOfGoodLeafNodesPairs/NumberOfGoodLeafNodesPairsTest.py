from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the1530_NumberOfGoodLeafNodesPairs.Solution import Solution


class Test(TestCaseBase):
    def atest(self, oj, distance, e):
        so = Solution()
        root = self.bt_from_OJ(oj)
        self.assertEquals(so.countPairs(root, distance), e)

    def test(self):
        atest = self.atest

        atest(oj='[1,2,3,null,4]', distance=3, e=1)
        atest(oj='[1,2,3,4,5,6,7]', distance=3, e=2)
        atest(oj='[7,1,4,6,null,5,3,null,null,null,null,null,2]', distance=3, e=1)
