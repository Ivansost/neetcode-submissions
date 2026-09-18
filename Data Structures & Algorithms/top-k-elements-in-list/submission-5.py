class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dickNum = {}
        outArr = []
        value = 0
        idx = []

        for i in nums:
            dickNum[i] = dickNum.get(i,0) + 1

        for j in range(k):

            value = 0
            best = None
            
            for key,val in dickNum.items():
                if val >= value and key not in idx:
                    value = val
                    best = key

            idx.append(best)
            outArr.append(best)

        return outArr
            


