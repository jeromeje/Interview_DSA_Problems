class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:      
        initial =0
        for i in range (0,len(nums)):
            if nums[i]!= val:
                nums[initial] = nums[i]
                initial+=1       
        return initial
