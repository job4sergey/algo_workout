import os

os.environ['NOMAIN'] = '1'
from com.mcc.ds_algs_course.graph.apsp.floyd_warshall.the01335_canteen.Solution2 import parse_and_run
from com.letcode.common.TestCaseBase import TestCaseBase


class FloydWarshallTest(TestCaseBase):
    def atest_file(self, in_file_path, e_out_file_path):
        class Solution:
            def process(self, in_file, out_file):
                parse_and_run(in_file, out_file)

        self.assert_from_file(Solution(), in_file_path, e_out_file_path)

    def test(self):
        atest_file = self.atest_file

        atest_file('in02.txt', 'out02.txt')
        atest_file('in01.txt', 'out01.txt')
