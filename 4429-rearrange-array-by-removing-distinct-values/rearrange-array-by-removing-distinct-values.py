class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        ans = []

        while nums:
            visited = set()
            remaining = []

            for x in nums:
                if x not in visited:
                    visited.add(x)
                    ans.append(x)
                else:
                    remaining.append(x)

            nums = remaining

        return ans