class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        outlist = []
        great = 0
        freq = 0
        
        #store all nums from array to a dictionary
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        #loop thorugh it and find the max
        for _ in range (k):
            #settng K to the value of bucket in dic
            for j in dic:
                if great <= dic[j]:
                    great = dic[j]
                    freq = j

            outlist.append(freq)
            dic.pop(freq,None)
            great = 0
           
        return outlist