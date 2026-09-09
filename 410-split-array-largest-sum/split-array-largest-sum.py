class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)

        def canSplit(largest):
            currSum = 0
            subarray = 1

            for i in range(n):
                if currSum + nums[i] > largest:
                    currSum = nums[i]
                    subarray += 1
                else:
                    currSum += nums[i]

            return subarray <= k

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res