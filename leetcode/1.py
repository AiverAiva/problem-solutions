class Solution(object):
    def twoSum(self, nums, target):
        qwq = {}
        for owo, uwu in enumerate(nums):
            pwp = target - uwu
            if uwu in qwq:
                return [owo, qwq[uwu]]
            qwq[pwp] = owo