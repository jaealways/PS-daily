"""
anagram끼리 묶어서 return

정렬해서 그 key 안에 넣기


"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictStr={}
        for s in strs:
            tmpS=''.join(sorted(s))
            if tmpS not in dictStr:
                dictStr[tmpS]=[]
            dictStr[tmpS].append(s)
        return dictStr.values()