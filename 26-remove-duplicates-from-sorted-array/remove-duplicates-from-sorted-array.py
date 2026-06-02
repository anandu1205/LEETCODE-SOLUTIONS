class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        r=1
        while l<len(nums) and r<len(nums):
            if nums[r]!=nums[r-1]:
              nums[l]=nums[r]
              l+=1
            r+=1
        return l
        