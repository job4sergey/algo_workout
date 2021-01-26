import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.arithmetics.extended_euclid.the03299_euclid.MccSolution import \
    solution
from com.letcode.common.TestCaseBase import TestCaseBase


class TaskCSaturdayTest(TestCaseBase):
    def atest(self, a, b, c, e):
        self.assertEquals(solution(a, b, c), e)

    def test(self):
        atest = self.atest

        # atest(1, 2, 3, (1, 1, 1))
        # atest(10, 6, 8, (2, 2, -2))
