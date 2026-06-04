class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        length=len(nums)
        if length<3:
            return []
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
               continue
            target=-a
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    list1=[a,nums[l],nums[r]]
                    #nothing
                    result.append(list1)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                      r -= 1
                elif nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
        return result 
        