class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                subarray=nums[i:j+1]
                visited=set()
                for k in subarray:
                    if k in visited:
                        continue
                    visited.add(k)
                length=len(visited)
                sum+=length**2
        return sum+len(nums)
                    

        