def characterReplacement(self, s: str, k: int) -> int:
    l=0
    dict1={}
    res=0
    maxf=0
    for r in range(len(s)):
        dict1[s[r]] = 1+dict1.get(s[r],0)
        maxf=max(maxf,dict1[s[r]])

        if (r-l+1) -maxf>k:
            dict1[s[l]]-=1            
            l+=1
        
        res =max(res,r-l+1)
    return res

"""sumary_line

Sliding Window
Q424
"""
