class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr={}
        
        for i in range(len(arr)):
            if arr[i] not in dict_arr:
                dict_arr[arr[i]]=0
            dict_arr[arr[i]]+=1
        
        temp=list(dict_arr.values())
        if len(temp)!=len(list(set(temp))):
            return False
        return True
                    