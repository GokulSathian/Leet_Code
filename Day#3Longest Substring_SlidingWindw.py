class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr1=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in substr1:
                substr1.remove(s[l])
                l+=1                   
            substr1.add(s[i])
            res=max(res,i-l+1)
        return res
            
