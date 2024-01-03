"""
이전 row 값의 1 * 다음 row값의 1 갯수만큼 곱

리스트 간의 갯수 count해서 

"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        array=[]
        m,n=len(bank[0]),len(bank)
        for i in range(n):
            num=0
            for j in range(m):
                if bank[i][j]=='1':
                    num+=1
            if num:
                array.append(num)
        if len(array)==1:
            return 0
        answer=0
        for i in range(1,len(array)):
            answer+=array[i-1]*array[i]
        return answer