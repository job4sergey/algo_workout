import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.stack.the_00756_WindowMin.MccSolution2 import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class WindowMinTest(TestCaseBase):
    def atest(self, ns, k, e):
        self.assertEquals(solution(ns, k), e)

    def test(self):
        atest = self.atest

        atest(self.s2a('1 3 2 4 5 3 1'), 3, self.s2a("""1
2
2
3
1"""))

        atest(self.s2a('1 3'), 3, [1])
        atest(self.s2a('1 2 3'), 3, [1])
        atest(self.s2a('1 2 3 4'), 3, [1, 2])

