class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1)>len(nums2):
            B,A=nums1,nums2
        else:
            A,B=nums1,nums2
        total=len(nums1)+len(nums2)
        half=total//2
        l,r=0,len(A)-1
        print(A,B)
        while True:
            i=(l+r)//2
            j=half-i-2
            Aleft_max = A[i] if i >= 0 else float("-infinity")
            Aright_min = A[i + 1] if (i + 1) <= (len(A)-1) else float("infinity")
            Bleft_max = B[j] if j >= 0 else float("-infinity")
            Bright_min = B[j + 1] if (j + 1) <= (len(B)-1) else float("infinity")

            if Aleft_max<=Bright_min and Bleft_max<=Aright_min:
                print(5/2)
                if total%2:
                    return min(Aright_min,Bright_min)
                print(max(Aleft_max,Bleft_max)+min(Aright_min,Bright_min))
                return ((max(Aleft_max,Bleft_max)+min(Aright_min,Bright_min))/2)
            
            elif Aleft_max>Bright_min:
                r=i-1
            elif Bleft_max>Aright_min:
                l=i+1


j=Solution()
x=j.findMedianSortedArrays([2],[])

print(x)

"""
Method1:l=nums1+nums2
l.sort()
mid=len(l)//2
median=(l[mid]+l[~mid])/2   #can't be used as Merging two array O(m+n)
return median

Using Bitwise Negation operator ~ 
a=3
~a=-4


Here O(log(m+n)) so binary search 

"""