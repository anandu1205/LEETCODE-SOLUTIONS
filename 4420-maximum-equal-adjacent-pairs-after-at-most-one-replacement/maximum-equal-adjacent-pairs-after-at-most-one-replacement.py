class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        n = len(nums)

        init = 0
        for i in range(len(nums) - 1):    
            if nums[i] == nums[i+1]:
                init += 1
            
        adj_counter = defaultdict(int)
        adj_counter[0] 

        if init == 0:
            adj_counter[(nums[0], nums[1])] = 1

        for i in range(1, len(nums) - 1):    
            if nums[i] != nums[i+1]:
                adj_counter[(nums[i], nums[i+1])] += 1
            if nums[i] != nums[i-1]:
                adj_counter[(nums[i], nums[i-1])] += 1

        if nums[-1] != nums[-2]:
            adj_counter[(nums[-1], nums[-2])] += 1

        return init + max(adj_counter.values())