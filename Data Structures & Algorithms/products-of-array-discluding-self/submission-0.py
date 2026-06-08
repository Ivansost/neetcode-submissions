class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prod inital to 1 since multiplying
        prod = 1
        #output array
        totalArray = []
        #loop thorugh the list to pop the element first
        for i in range(len(nums)):
            remove = nums.pop(i)
            ##reset the prod variable for each new itreration of the for loop
            prod = 1
            #loop through the remaining elemnts in the list
            for j in range(len(nums)):
                #store the product each time when multiply by next element
                prod = prod * nums[j]
            #add the final prod for this inner forloop to the output array
            totalArray.append(prod)
            #put our number we poped back
            nums.insert(i,remove)
        
        return totalArray