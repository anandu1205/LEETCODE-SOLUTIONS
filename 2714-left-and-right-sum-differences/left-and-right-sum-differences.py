class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftSum=[0]*n
        rightSum=[0]*n
        answer=[0]*n
        
        for i in range(n):
            if i==0:
                leftSum[i]=0
                rightSum[i]=sum(nums[i+1:])
                answer[i]=abs(leftSum[i]-rightSum[i])
            if i==n-1:
                leftSum[i]=sum(nums[0:i])
                rightSum[i]=0
                answer[i]=abs(leftSum[i]-rightSum[i])
            else:
                leftSum[i]=sum(nums[0:i])
                rightSum[i]=sum(nums[i+1:])
                answer[i]=abs(leftSum[i]-rightSum[i])
        return answer

        