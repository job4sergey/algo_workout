class NumArray(object):

    def __init__(self, nums):
        r = 0
        self.pre = []
        for n in nums:
            r += n
            self.pre.append(r)

    def sumRange(self, i, j):
        return self.pre[j] - (self.pre[i - 1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
