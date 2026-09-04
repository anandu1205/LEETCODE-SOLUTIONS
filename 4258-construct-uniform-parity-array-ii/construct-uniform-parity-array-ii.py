class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n=len(nums1)
        even_count=0
        odd_count=0
        for num in nums1:
            if num%2==0:
                even_count+=1
            else:
                odd_count+=1
        if even_count==n or odd_count==n:
            return True
        minimum=min(nums1)
        if minimum%2==0:
            return False
        if minimum%2!=0:
            return True