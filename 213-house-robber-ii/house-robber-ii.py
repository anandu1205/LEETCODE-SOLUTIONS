class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        
        arr1=nums[:-1]
        arr2=nums[1:]
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)
        dp1[0]=arr1[0]
        dp1[1]=max(arr1[0],arr1[1])
        dp2[0]=arr2[0]
        dp2[1]=max(arr2[0],arr2[1])
        for i in range(2,len(nums)-1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+arr1[i])

            dp2[i]=max(dp2[i-1],dp2[i-2]+arr2[i])
        return max(dp1[-1],dp2[-1])