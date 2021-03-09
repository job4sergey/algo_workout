import os
from collections import Counter
import copy

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.stack.the_00051_CorrectBracketSequence.MccSolution import solution

from com.letcode.common.TestCaseBase import TestCaseBase


class ContainersTest(TestCaseBase):
    def atest(self, s, e):
        self.assertEquals(solution(s), e)

    def test(self):
        atest = self.atest

        atest('()[]', True)
