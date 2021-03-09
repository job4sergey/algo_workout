import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.dp.the_07_substrings.task_d_491_almost_palindrom.MccSolution import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class AlmostPalindromTest(TestCaseBase):
    def atest(self, s, k, e):
        self.assertEquals(solution(s, k), e)

    def test(self):
        atest = self.atest

        atest('abcde', 1, 12)
        atest('aaa', 3, 6)
