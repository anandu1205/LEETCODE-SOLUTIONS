class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        sorted_arr = sorted(arr)
        rank = {}
        curr_rank = 1

        rank[sorted_arr[0]] = 1

        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] != sorted_arr[i - 1]:
                curr_rank += 1
            rank[sorted_arr[i]] = curr_rank

        return [rank[x] for x in arr]