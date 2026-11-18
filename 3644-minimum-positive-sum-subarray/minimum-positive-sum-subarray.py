class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        minimum_sum = float('inf')

        for pointer in range(len(nums)):
            for i in range(l, r+1):

                if pointer+i <= len(nums):
                    subarray = nums[pointer:pointer+i]
                    subarray_sum = sum(subarray)

                    if subarray_sum > 0:
                        minimum_sum = min(minimum_sum, subarray_sum)

        return minimum_sum if minimum_sum != float('inf') else -1