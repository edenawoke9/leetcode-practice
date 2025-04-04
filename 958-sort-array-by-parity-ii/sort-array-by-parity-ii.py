class Solution(object):
    def sortArrayByParityII(self, nums):
        even_idx, odd_idx = 0, 1
        n = len(nums)
        
        while even_idx < n and odd_idx < n:
            if nums[even_idx] % 2 == 0:
                even_idx += 2  
            elif nums[odd_idx] % 2 == 1:
                odd_idx += 2  
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 2
                odd_idx += 2
        
        return nums

