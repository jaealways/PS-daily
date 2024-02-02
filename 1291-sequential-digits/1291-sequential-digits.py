"""
low, high 사이에서 연속된 숫자

low len, high len: len+low_len~high까지
10^9 승까지 가능, 모든 숫자 생성하는 건 x



"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nl,nh=len(str(low)),len(str(high))
        array=[]
        for n in range(nl,nh+1):
            for m in range(1,11-n):
                tmp=[str(x) for x in range(m,m+n)]
                tmp=int(''.join(tmp))
                if tmp>high:
                    break
                elif low<=tmp:
                    array.append(tmp)
        return array
                