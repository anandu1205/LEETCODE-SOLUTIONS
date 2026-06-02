class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length1=len(nums1)
        length2=len(nums2)
        r=-1
        l=0
        while not r<-length2:
            nums1[r]=nums2[l]
            r=r-1
            l=l+1
        nums1.sort()
        