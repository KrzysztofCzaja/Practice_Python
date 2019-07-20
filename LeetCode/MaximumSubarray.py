# https://leetcode.com/problems/maximum-subarray/
#FIRST O(n)
class Solution:
    def maxSubArray(self, nums) -> int:
        total, best = 0,nums[0]
        for i in nums:
            total += i
            if total>best: best = total
            if total < 0: total = 0
        return best
#SECOND

# class Solution:
#     def maxSubArray(self, nums) -> int:
#         for i in range(1,len(nums)):
#                 nums[i] = max(nums[i - 1] + nums[i], nums[i])
#         return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))