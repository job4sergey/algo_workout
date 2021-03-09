import os
from collections import Counter
import copy

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.stack.the_00053_Containers.MccSolution2 import solution

from com.letcode.common.TestCaseBase import TestCaseBase


class ContainersTest(TestCaseBase):
    def atest_cant(self, sts):
        acts = solution(sts)
        self.assertTrue(acts is None)

    def atest(self, sts):
        sts0 = copy.deepcopy(sts)
        gfq = Counter()
        for i, st in enumerate(sts0):
            gfq.update(Counter(st))

        acts = solution(sts)
        for fro, to in acts:
            if not sts0[fro]:
                self.assertTrue(False, 'Src empty')

            x = sts0[fro].pop()
            sts0[to].append(x)

        for i, st in enumerate(sts0):
            fq = Counter(st)
            if len(fq) != 1:
                self.assertTrue(False, 'Unexpected vals:%s ' % sts0)

            if fq[i + 1] != gfq[i + 1]:
                self.assertTrue(False, 'Unexpected value:%s ' % sts0)

    def test(self):
        atest = self.atest
        atest_cant = self.atest_cant

        atest([
            [3, 2, 1],
            [1, 2, 3],
            [1, 2, 3],
        ])

        atest([
            [3],
            [1],
            [2],
        ])

        atest([
            [1],
            [3],
            [2],
        ])

        atest([
            [],
            [1, 2, 3],
            [1, 2, 3, 3, 2, 1],
        ])

        atest([
            [],
            [],
            [1, 2, 3, 3, 2, 1, 1, 2, 3],
        ])

        atest([
            [1],
        ])

        atest([
            [1, 1],
            [2]
        ])

        atest_cant([
            [2, 1],
            [2]
        ])

        atest([
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ])

        atest([
            [4, 2, 3, 1],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ])

        atest([
            [4, 2, 3, 1],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [5]
        ])

        atest([
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
        ])

        atest([
            [1],
            [2],
            [3]
        ])

        atest([
            [1, 1],
            [2],
            [3]
        ])

        atest([
            [1, 2, 3, 2],
            [],
            []
        ])

        atest([
            [1, 1, 1, 2, 3],
            [],
            []
        ])

        atest([
            [1, 3, 2, 1, 3],
            [],
            []
        ])

        atest([
            [1, 2, 2, 2],
            []
        ])

        atest_cant([
            [2, 1, 2, 2, 2],
            []
        ])
