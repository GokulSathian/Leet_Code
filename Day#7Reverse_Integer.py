class Solution:
    def reverse(self, x: int) -> int:
        MIN=-2**31
        MAX=(2**31)-1
        var=0
        while x:
            digit=int(math.fmod(x,10))
            x=int(x/10)
            var=var*10+digit
            if var>MAX:
                return 0
            elif var<MIN:
                return 0
            print(var)

        return var  