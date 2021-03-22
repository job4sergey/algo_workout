# theirs idea, track open / closing bracket count
class Solution(object):
    def minAddToMakeValid(self, s):
        lcn, rcn = 0, 0

        for c in s:
            if c == '(':
                lcn += 1
            else:
                if lcn:
                    lcn -= 1
                else:
                    rcn += 1

        return lcn + rcn
