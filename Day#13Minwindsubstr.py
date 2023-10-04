def minWdefindow(self, s: str, t: str) -> str:
    dict_t,dict_s={},{}
    l=0

    if t=="": 
        return ""

    for i in t:
        dict_t[i] =1+dict_t.get(i,0)
    
    have, need =0, len(dict_t)
    indx,len_index=[-1,-1],float("infinity")    #should be -1,-1 or else indx gets out of range at the end also len indx to find smaller windws

    for j in range(len(s)):
        dict_s[s[j]] =1+dict_s.get(s[j],0)

        if s[j] in dict_t and dict_s[s[j]]==dict_t[s[j]]:
            have+=1

        while have == need:
            if (j-l+1)<len_index:
                indx=[l,j]
                len_index=(j-l+1)
            dict_s[s[l]]-=1
            if s[l] in dict_t and dict_s[s[l]]<dict_t[s[l]]:
                have-=1
            l+=1
    print(indx)
    return s[indx[0]:indx[1]+1]



"""sumary_line

Sliding Window
Airbnb Q
76
"""
