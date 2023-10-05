from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        return [num for num, count in Counter(nums).items() if count > len(nums) // 3]

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        