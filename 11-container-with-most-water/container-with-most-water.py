class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max=0
        while left<right and 0<=left<len(height) and 0<=right<len(height):
            no_of_gaps=right-left
            min_height=min(height[left],height[right])
            water_trapped=min_height*no_of_gaps
            if water_trapped>max:
                max=water_trapped
            if min_height==height[left]:
                    left+=1
            if min_height==height[right]:
                    right-=1
        return max
        