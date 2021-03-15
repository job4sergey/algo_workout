from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the1441_BuildAnArrayWithStackOperations.Solution import Solution


class Test(TestCaseBase):
    def atest(self, target, n, e):
        so = Solution()
        self.assertEquals(so.buildArray(target, n), e)

    def test(self):
        atest = self.atest

        atest(target=[1, 3], n=3, e=["Push", "Push", "Pop", "Push"])
        atest(target=[1, 2, 3], n=3, e=["Push", "Push", "Push"])
        atest(target=[1, 2], n=4, e=["Push", "Push"])
        atest(target=[2, 3, 4], n=4, e=["Push", "Pop", "Push", "Push", "Push"])
