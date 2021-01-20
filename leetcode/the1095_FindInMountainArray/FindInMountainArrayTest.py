from com.letcode.common.TestCaseBase import TestCaseBase
from com.letcode.the1095_FindInMountainArray.Solution2 import Solution


class Test(TestCaseBase):
    class Arr:
        def __init__(self, a):
            self.a = a

        def get(self, i):
            return self.a[i]

        def length(self):
            return len(self.a)

    def atest(self, t, arr, e):
        so = Solution()
        self.assertEquals(so.findInMountainArray(t, self.Arr(arr)), e)

    def test(self):
        atest = self.atest

        atest(0, [1, 5, 2], -1)
        atest(1, [0, 5, 3, 1], 3)
        atest(arr=[1, 2, 3, 4, 5, 3, 1], t=3, e=2)
        atest(arr=[0, 1, 2, 4, 2, 1], t=3, e=-1)
