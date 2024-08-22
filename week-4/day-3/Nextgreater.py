class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        sub_set = []
        
        for num in reversed(nums2):
            while sub_set and sub_set[-1] <= num:
                sub_set.pop()
            next_greater[num] = sub_set[-1] if sub_set else -1
            sub_set.append(num)
        
        return [next_greater[num] for num in nums1]
        