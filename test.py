class Solution:
    def longestPalindrome(self, s: str) -> str:
        l,r=0,len(s)-1
        collection=[]
        count=0

        if len(s)==1:
            collection.append(s)

        for l in range(len(s)-1):
            front,end="",""
            print(l,r)
            while r>=l:
                if s[l] ==s[r]:
                    print("in")
                    string1=s[l:r+1]
                    if string1 == string1[::-1]:
                        collection.append(string1)
                r-=1              
            r=len(s)-1
        return max(collection,key=len)
    
x=Solution()
j=x.longestPalindrome("a")
print(j)