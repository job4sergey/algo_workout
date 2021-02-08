from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the0223_RectangleArea.Solution2 import Solution


class Test(TestCaseBase):
    def atest(self, A, B, C, D, E, F, G, H, e1):
        s = Solution()
        self.assertEquals(s.computeArea(A, B, C, D, E, F, G, H), e1)
        self.assertEquals(s.computeArea(E, F, G, H, A, B, C, D), e1)

    def test(self):
        atest = self.atest

        atest(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2, e1=45)
