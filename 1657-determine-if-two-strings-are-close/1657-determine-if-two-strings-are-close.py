"""
swap, transform 가능

boolean으로 예측하는 문제니까, 
위치 정보는 신경 안써도 됨
transform 시 두 개를 서로 바꿔야 함

dict 상에 알파벳은 서로 간에 바꿀 수 있음
구성과 길이만 같으면, 바꾸는 거니까 언제든 transform 가능


"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1,dict2={},{}
        for i in range(len(word1)):
            if word1[i] not in dict1:
                dict1[word1[i]]=0
            dict1[word1[i]]+=1
        for i in range(len(word2)):
            if word2[i] not in dict2:
                dict2[word2[i]]=0
            dict2[word2[i]]+=1
        if dict1.keys()!=dict2.keys():
              return False
        array1=sorted(list(dict1.values()))
        array2=sorted(list(dict2.values()))
        if array1!=array2:
            return False
        return True
        