class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i,j in enumerate(nums):
            if target-j in x:
                return [i,x[target-j]]
            x[j]=i


"""
Using Dictinory/Hashmap
enumerate
"""
