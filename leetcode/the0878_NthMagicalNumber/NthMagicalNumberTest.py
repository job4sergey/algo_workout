from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0878_NthMagicalNumber.Solution import Solution


class Test(TestCaseBase):
    def atest(self, n, a, b, e):
        so = Solution()
        self.assertEquals(so.nthMagicalNumber(n, a, b), e)

    def test(self):
        atest = self.atest

        atest(n=1, a=2, b=3, e=2)
        atest(n=4, a=2, b=3, e=6)
        atest(n=5, a=2, b=4, e=10)
        atest(n=3, a=6, b=4, e=8)
