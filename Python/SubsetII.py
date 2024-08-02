class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)

            curr.pop()
            while (i < len(nums) - 1 and nums[i] == nums[i+1]):
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res