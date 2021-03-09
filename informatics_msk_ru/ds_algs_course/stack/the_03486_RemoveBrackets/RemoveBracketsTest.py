import os

os.environ['NOMAIN'] = '1'
from com.mcc.tasks.the_03486_RemoveBrackets.MccSolution2 import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class TaskCSaturdayTest(TestCaseBase):
    def atest(self, s, e):
        self.assertEquals(solution(s), e)

    def test(self):
        atest = self.atest

        atest('())(()', 2)
        atest('))(((', 5)
