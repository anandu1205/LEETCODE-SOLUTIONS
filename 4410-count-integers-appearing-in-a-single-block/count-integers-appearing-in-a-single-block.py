class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        special=0
        maximum={}
        minimum={}
        for i in range(len(nums)):
            value=nums[i]
            minimum[value]=nums.index(value)
        for i in range(len(nums)):
            value=nums[i]
            value1=minimum[value]
            arr=nums[i:]
            for j in range(len(arr)):
                if (j+i)>value1 and arr[j]==value:
                    value1=j+i
            maximum[value]=value1
        visited=set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            value=nums[i]
            if (maximum[value]-minimum[value]+1)==nums.count(value):
                special+=1
        return special