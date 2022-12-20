class Solution(object):
    def sortColors(self, nums):
        if len(nums)==1:
            return nums
        m0=nums.count(0)
        m1=m0+nums.count(1)
        m2=m1+nums.count(2)
        j=0
        while(j<len(nums)):
            if j<m0:
                nums[j]=0
            elif j<m1:
                nums[j]=1
            elif j<m2:
                nums[j]=2
            j=j+1
        return nums