#SOL1 binary search
#Runtime 3 ms Beats 99.78%
#Memory 13.2 MB Beats 73.85%
class Solution(object):
    def isPerfectSquare(self, num):
        if(num==1): return True
        start, end=0, num//2
        while(start<=end):
            i=(start+end)//2
            sq=i*i
            if(sq==num):
                return True
            elif(sq>num):
                end=i-1
            elif(sq<num):
                start=i+1
        return False

        """
        :type num: int
        :rtype: bool
        """
        

#SOL2
#Runtime 19 ms Beats 22.97%
#Memory 13.1 MB Beats 73.85%
class Solution(object):
    def isPerfectSquare(self, num):
        start=1
        while(start*start<num):
            start+=1
        
        if(start*start==num):
            return True
        else:
            return False

        """
        :type num: int
        :rtype: bool
        """
        