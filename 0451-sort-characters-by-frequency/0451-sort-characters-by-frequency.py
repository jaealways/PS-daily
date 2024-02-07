"""
돌면서 dict에서 count

정수:[a,b] 꼴로 다시 변환
정수 key list 뽑아서 정렬 후, value * key 해서 출력

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        count=Counter(s)
        list_char=sorted(count.keys(), key=lambda x:(-count[x]))
        return ''.join(char*count[char] for char in list_char)
        
        