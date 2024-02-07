"""
돌면서 dict에서 count

정수:[a,b] 꼴로 다시 변환
정수 key list 뽑아서 정렬 후, value * key 해서 출력

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        dict_count,dict_num={},{}
        for char in s:
            dict_count[char]=dict_count.get(char,0)+1
        for key,val in dict_count.items():
            if val not in dict_num:
                dict_num[val]=[]
            dict_num[val].append(key)
        list_count=sorted(list(dict_num.keys()), reverse=True)
        answer=[]
        for n in list_count:
            tmp=dict_num[n]
            tmp=[c*n for c in tmp]
            answer=answer+tmp
        return ''.join(answer)
        
        