class Solution1:
    def search(self, nums: list[int]) -> int:
        res = 0
        l = 0
        r = len(nums) - 1
        while (l <= r):
            if (nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if(nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

test = Solution1()
print(test.search([3, 4, 5, 6, 1, 2]))