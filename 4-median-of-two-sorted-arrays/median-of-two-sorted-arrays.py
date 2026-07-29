class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        ans=nums1+nums2
        ans.sort()
        n=len(ans)
        if n%2==1:
            med=(0+n-1)/2
            return ans[int(med)]
        else:
            med=(0+n-1)/2
            left=math.floor(med)
            right=math.ceil(med)
            return (ans[left]+ans[right])/2
        