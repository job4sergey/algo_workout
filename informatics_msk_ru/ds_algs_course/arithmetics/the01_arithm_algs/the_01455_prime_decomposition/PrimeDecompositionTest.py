import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.arithmetics.the01_arithm_algs.the_01455_prime_decomposition.MccSolution2 import \
    solution
from com.letcode.common.TestCaseBase import TestCaseBase


class PrimeDecompositionTest(TestCaseBase):
    def atest(self, n, e):
        self.assertEquals(solution(n), e)

    def test(self):
        atest = self.atest

        atest(1008, '2^4*3^2*7')
        atest(1024, '2^10')
        atest(32, '2^5')
        atest(2, '2')

        # atest(1, 2, 3, (1, 1, 1))
        # atest(10, 6, 8, (2, 2, -2))
