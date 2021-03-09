import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.stack.the_111648_Balls.MccSolution2 import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class BallsTest(TestCaseBase):
    def atest(self, ns, e):
        self.assertEquals(solution(ns), e)

    def test(self):
        atest = self.atest

        atest(self.s2a('3 3 2 1 1 1 2 2 3 3'), 10)
        atest(self.s2a('1 3 3 3 2'), 3)
