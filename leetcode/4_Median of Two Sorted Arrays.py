class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        all = sorted(nums1 + nums2)
        if len(all) % 2 != 0:
            return float(all[len(all) // 2])
        else:
            return (all[len(all) // 2 - 1] + all[len(all) // 2]) / 2.0