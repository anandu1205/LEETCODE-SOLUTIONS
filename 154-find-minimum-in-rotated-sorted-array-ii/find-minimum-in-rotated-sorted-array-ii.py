class Solution:
    def findMin(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        while nums[0]!=min(nums):
            nums[0]=nums[n-1]
            for i in range(1,n):
                nums[i-1]=nums[i]
            count=count+1
        return min(nums)              