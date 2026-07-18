class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum=max(nums)
        minimum=min(nums)
        while minimum:
            maximum,minimum=minimum,maximum%minimum
        return maximum
        