class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            new_max = max(x, max_prod * x, min_prod * x)
            new_min = min(x, max_prod * x, min_prod * x)

            max_prod = new_max
            min_prod = new_min

            ans = max(ans, max_prod)

        return ans
        