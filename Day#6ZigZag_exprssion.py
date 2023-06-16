class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str1=""
        var=1
        incr=(numRows-1)*2
        if numRows==1:
            return s
        for r in range(numRows):
            for i in range(r,len(s),incr):
                str1+=s[i]
                print(i,s[i])
                if r!=0 and r<(numRows-1) and i+incr-2*r<len(s):
                    print(i+incr-2*r,s[i+incr-2*r])
                    str1+=s[i+incr-2*r]
                
        return(str1)     