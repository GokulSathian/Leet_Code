class Solution:
    def convert(self, s: str, numRows: int) -> str:
        List1=[]
        str1=""
        if numRows==1:
            return s
        for j in range(numRows):
            List1.append("")
        pointer=0
        var=1
        for i in range(len(s)):
            List1[pointer] = List1[pointer]+s[i]
            pointer=pointer+var 
            print(pointer,numRows)  
            if pointer==numRows-1:
                var*=-1
            elif pointer==0:
                var*=-1
                  

        for j in List1:
            str1+=j
        return str1
            

    
x=Solution()
print(x.convert("PALINDROME",3))