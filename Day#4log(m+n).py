class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l=nums1+nums2
        l.sort()
        mid=len(l)//2
        median=(l[mid]+l[~mid])/2   #can't be used as Merging two array O(m+n)
        return median


j=Solution()
x=j.findMedianSortedArrays([2],[])
print(x)