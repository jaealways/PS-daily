class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dictNum={}
        for i in nums:
            dictNum[i]=dictNum.get(i,0)+1
        maxval,count=0,0
        for val in dictNum.values():
            if val>maxval:
                maxval,count=val,1
            elif val==maxval:
                count+=1
        return count*maxval
