import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.arithmetics.gcd_lcm_reduceable_tasks.task_f__ratio.MccSolution import \
    solution
from com.letcode.common.TestCaseBase import TestCaseBase


class RatioTest(TestCaseBase):
    def atest(self, n, e):
        self.assertEquals(solution(n), e)

    def test(self):
        atest = self.atest

        atest(23, (11, 12))
        atest(10, (3, 7))
        # atest(10, 6, 8, (2, 2, -2))
