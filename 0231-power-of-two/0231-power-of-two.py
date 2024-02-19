"""
계속 2로 나누다가 몫 0, 나머지 1이면 return True

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        d,r=divmod(n,2)
        while d>0 and r==0:
            d,r=divmod(d,2)
        if d==0 and r==1:
            return True
        return False