class Solution(object):
    def myPow(self, x, n):
        result = 1
        negative=False
        if n < 0: negative = True

        n = abs(n)
        while n != 0:
            if n%2 == 0:
                x = x*x
                n = n//2
            else:
                result = result*x
                n = n-1

        if negative:
            return 1/result
        return result
        
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        