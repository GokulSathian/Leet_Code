def search(self, nums: List[int], target: int) -> int:
    l,r=0,len(nums)-1

    while l<=r:
        mid=l+(r-l)//2      #l+ because lies to the left of pointer and count starts from left
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            return(mid)
    return-1
                

"""sumary_line

Binary Search
Q.704
"""
