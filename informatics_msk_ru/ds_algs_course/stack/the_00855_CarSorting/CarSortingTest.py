import os

os.environ['NOMAIN'] = '1'
from com.mcc.tasks.the_00855_CarSorting.MccSolution import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class TaskCSaturdayTest(TestCaseBase):
    def atest(self, cars, e):
        self.assertEquals(solution(cars), e)

    def test(self):
        atest = self.atest

        atest([3, 2, 1], [(1, 3), (2, 3)])
        atest([2, 3, 1], None)
        atest([4, 1, 3, 2], [(1, 2), (2, 1), (1, 2), (2, 3)])
