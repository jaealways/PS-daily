"""
5: 101
6: 110
7: 111
    100

"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i=0
        while left!=right:
            left=left>>1
            right=right>>1
            i+=1
        return left<<i