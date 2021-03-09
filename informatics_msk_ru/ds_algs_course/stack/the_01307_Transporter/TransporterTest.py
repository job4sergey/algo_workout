import os
from collections import Counter
import copy

os.environ['NOMAIN'] = '1'
from com.letcode.common.TestCaseBase import TestCaseBase
from com.mcc.ds_algs_course.stack.the_01307_Transporter.MccSolution import solution


class TransporterTest(TestCaseBase):
    def atest(self, cs, e):
        self.assertEquals(solution(cs), bool(e))

    def test(self):
        atest = self.atest

        atest([2.9, 2.1], 1)
        atest([5.6, 9.0, 2.0], 0)
