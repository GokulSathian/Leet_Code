def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    rows,column=len(matrix),len(matrix[0])
    top,bottom=0,rows-1
    while top<=bottom:
        mid=top+(bottom-top)//2  #prevent overflow
        if matrix[mid][-1]<target:
            top=mid+1
        elif matrix[mid][0]>target:
            bottom=mid-1
        else:
            break
    if not (top<=bottom):
        return False
    row=(top+bottom)//2

    l,r=0,column-1
    while l<=r:
        mid=l+(r-l)//2  #prevent overflow
        if matrix[row][mid]<target:
            l=mid+1
        elif matrix[row][mid]>target:
            r=mid-1
        else:
            return True

    return False      

"""sumary_line

Binary Search
first in rowwise to select the row and then in columnwise  to find the number
Q.74
"""
