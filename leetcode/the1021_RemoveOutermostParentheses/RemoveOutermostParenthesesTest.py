from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the1021_RemoveOutermostParentheses.Solution3 import Solution


class Test(TestCaseBase):
    def atest(self, S, e):
        so = Solution()
        self.assertEquals(so.removeOuterParentheses(S), e)

    def test(self):
        atest = self.atest

        atest("(()())(())", "()()()")
        atest("(()())(())(()(()))", "()()()()(())")
        atest("()()", "")
