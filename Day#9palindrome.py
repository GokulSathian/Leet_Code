class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        start,trail=0,len(s)-1
        while start<trail:
            print(s[start],s[trail])
            if s[start]!=s[trail]:
                return False
            start+=1
            trail-=1
        return True

x=Solution()
print(x.isPalindrome(-234))