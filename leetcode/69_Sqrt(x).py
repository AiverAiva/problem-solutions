#SOL1 (OPTIMIZED BINARY SEARCH)
class Solution(object):
    def mySqrt(self, x):
        if x == 1 or x == 0: return x
        start=1
        end=x/2+1
        while(start<=end):
            mid = int(start+(end-start)/2)
            if(mid == x / mid):
                return mid
            elif(mid < x / mid):
                start = mid + 1
            else:
                end = mid - 1
        return end

#SOL2
class Solution(object):
    def mySqrt(self, x):
        if x == 1 or x == 0: return x
        i=1
        while(i*i<=x):
            i+=1
        return i-1
        