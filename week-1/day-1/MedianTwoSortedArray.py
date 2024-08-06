class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1+len2
        lst = nums1+nums2
        lst.sort()
        if total_len % 2 == 0:
            median = (lst[total_len // 2 - 1] + lst[total_len // 2])/2
        else:
            median = lst[total_len // 2]
        
        return median