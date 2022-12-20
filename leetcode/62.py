class Solution(object):
    def uniquePaths(self, m, n):
        step = 0
        a = 1
        b = 1
        for i in range(m-1):
            z = m-1+n-1
            a *= (z-i)
            b *= (i+1)
        return a/b