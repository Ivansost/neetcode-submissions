class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        total = 0
        previous = {}

        for num in nums:
            total+=num

            if total == k:
            #update our count if the total for the subarray adds to our k
                count += 1

            needed = total - k
            count += previous.get(needed, 0)
            previous[total] = previous.get(total, 0) + 1

        return count