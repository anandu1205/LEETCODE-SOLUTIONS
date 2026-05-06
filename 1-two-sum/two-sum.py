class Solution:
    def twoSum(self, nums, target):
        length = len(nums)

        for i in range(length):
            other = target - nums[i]

            if other in nums:
                index = nums.index(other)

                if index != i:
                    return [i, index]
        