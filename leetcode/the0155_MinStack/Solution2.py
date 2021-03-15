class MinStack:

    def __init__(self):
        self.st = []
        self.mn_st = [float('inf')]

    def push(self, x: int) -> None:
        self.st.append(x)
        mn_st = self.mn_st
        if mn_st[-1] >= x:
            mn_st.append(x)

    def pop(self) -> None:
        mn_st = self.mn_st

        x = self.st.pop()
        if x == mn_st[-1]:
            mn_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn_st[-1]
