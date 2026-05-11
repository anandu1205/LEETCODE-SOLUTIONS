class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            string=str(nums[i])
            for ch in string:
                result.append(int(ch))
        return result