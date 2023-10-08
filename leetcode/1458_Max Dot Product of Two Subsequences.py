# Runtime
# 144ms
# Beats 100.00%of users with Python

# Memory
# 13.12MB
# Beats 100.00%of users with Python

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [float('-inf')] * (n+1)
        for i in range(m):
            prev = float('-inf')
            for j in range(n):
                product = nums1[i] * nums2[j]
                prev, dp[j+1] =  dp[j+1], max(dp[j+1], dp[j], product, prev + product)
        return dp[-1]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        