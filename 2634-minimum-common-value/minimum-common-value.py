class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)

        minimum = float('inf')

        for num in nums1:
            if num in s and num < minimum:
                minimum = num

        return minimum if minimum != float('inf') else -1