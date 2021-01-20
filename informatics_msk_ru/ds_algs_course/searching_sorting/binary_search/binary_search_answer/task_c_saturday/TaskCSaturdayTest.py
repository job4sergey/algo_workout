import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.searching_sorting.binary_search.binary_search_answer.task_c_saturday.MccSolution import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class TaskCSaturdayTest(TestCaseBase):
    def atest(self, R, C, hs, e):
        self.assertEquals(solution(len(hs), R, C, hs), e)

    def test(self):
        atest = self.atest

        atest(2, 3, [170, 205, 225, 190, 260, 130, 225, 160], 30)
