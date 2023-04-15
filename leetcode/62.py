class Solution(object):
    def uniquePaths(self, m, n):
        step, a, b = 0, 1, 1
        for i in range(m-1):
            z = m-1+n-1
            a *= (z-i)
            b *= (i+1)
        return a/b
