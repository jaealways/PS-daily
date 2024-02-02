"""
low, high 사이에서 연속된 숫자

low len, high len: len+low_len~high까지
10^9 승까지 가능, 모든 숫자 생성하는 건 x



"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sl,sh=str(low),str(high)
        nl,nh=len(sl),len(sh)
        array=[]
        mapper="123456789"
        for i in range(nl,nh+1):
            for j in range(10-i):
                tmp=int(mapper[j:i+j])
                if tmp>high:
                    break
                elif low<=tmp:
                    array.append(tmp)
        
        return array
                