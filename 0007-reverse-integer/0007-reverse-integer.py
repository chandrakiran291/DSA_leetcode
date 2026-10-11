class Solution:
    def reverse(self, x: int) -> int:
        # result = 0
        # if x<0:
        #     x = (-1)*x
        #     string = str(x)
        #     reversed_string = "-" + string[::-1]
        #     result = int(reversed_string)
        # else:
        #     string = str(x)
        #     result = int(string[::-1])
        

        # if result< -2**31 or result>=2**31:
        #     return 0
        # return result
        result = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x>0:
            remainder = x%10
            result = result*10 + remainder
            x //= 10

        
        result = result*sign 
    
        if result<-2**31 or result>2**31:
            return 0
        
        return result

