class Solution:
    def reverse(self, x: int) -> int:
        mul=1
        MIN=-2^31
        MAX=(2^31)-1
        var=0
        if x<0:
            mul*=-1
            x*=-1
        elif x==0:
            return x

        while x>0:
            i=x%10
            x=x//10
            var=var*10+i
        print(var)

        return var*mul            