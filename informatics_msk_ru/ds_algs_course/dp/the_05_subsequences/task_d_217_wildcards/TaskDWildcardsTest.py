import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.dp.the_05_subsequences.task_d_217_wildcards.MccSolution3 import \
    solution

from com.letcode.common.TestCaseBase import TestCaseBase


class TaskDWildcardsTest(TestCaseBase):
    def atest(self, s1, s2, e):
        self.assertEquals(solution(s1, s2), e)
        self.assertEquals(solution(s2, s1), e)

    def test(self):
        atest = self.atest

        atest('*', '*', '')
        atest('??', '*', 'ZZ')
        atest('??', '?', 'No solution!')
        atest('ABCDEFG', 'ABCDEFG', 'ABCDEFG')
        atest('ABCD??G', 'ABCD*G', 'ABCDZZG')
        atest('ABCD??G', 'ABCD*G', 'ABCDZZG')
        atest('ABCDE?G', 'ABCDEFG', 'ABCDEFG')
        atest('A??D', 'A??D', 'AZZD')
        atest('A*D', 'AB?D', 'ABZD')
        atest('A?', 'B?', 'No solution!')
        atest('A?', 'A?', 'AZ')
        atest('?', '?', 'Z')
        atest('A?', 'AD', 'AD')
        atest('D', 'D', 'D')
        atest('AB*C*D', 'A*BCD', 'ABCD')
        atest('*D', 'D*', 'D')
        atest('*D', 'D', 'D')
        atest('ABC*D', 'A*BCD', 'ABCD')
        atest('ABC', 'ABC', 'ABC')
        atest('DAB?', '*BC', 'DABC')
        atest('AB?', '*BC', 'ABC')
