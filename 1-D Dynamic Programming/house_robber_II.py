class Solution:
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
    
    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2