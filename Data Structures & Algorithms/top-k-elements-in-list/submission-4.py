class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        outlist = []
        great = 0
        freq = 0
        
        #store all nums from array to a dictionary
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        #loop thorugh k times
        for _ in range (k):
            #loop though the dictonary
            for j in dic:
                #check if the value of the bucket is greater, if so set it to our max variable
                if dic[j] > great:
                    great = dic[j]
                    #also since its greater we set the freq variable to the bucket number
                    freq = j
            #since loop ends, we append the greatest num to the list
            outlist.append(freq)
            #remove it from dictionary so we dont use again
            dic.pop(freq,None)
            #reset our greatest variable
            great = 0
        #return the final list
        return outlist