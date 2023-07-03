class Solution:
    def myAtoi(self, s: str) :
        x=s.strip()
        if not x:
            return 0
        i=0
        parsed=0
        sign=1
        if x[i]=="-":
            sign*=-1
            i+=1
        elif x[i]=="+":
            i+=1
        while i<len(x) and x[i].isdigit():
            parsed=parsed*10+int(x[i])
            i+=1
        parsed=parsed*sign
        parsed = max(min(parsed, 2 ** 31 - 1), -2 ** 31)
        return parsed
        
        
x=Solution()
z=x.myAtoi(" ")
print(z)