class Solution(object):
    def climbStairs(self, n):
        li = {1: 1, 2: 2}
        for i in range(3, 46):
            li[i] = li[i-1] + li[i-2]
        return li[n]
        