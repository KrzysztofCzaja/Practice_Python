# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#FIRST O(n^2)?
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         i = 0
#         while i <len(nums):
#             a = nums[i]
#             b = (nums[i+1] if (i + 1) < len(nums) else None)
#             if a == b:
#                  nums.remove(nums[i])
#             else:
#                 i += 1
#         return len(nums)
#
# #SECOND worst than before, even O(n^3)?
# class Solution:
#     def removeDuplicates(self,nums)-> int:
#         i = 0
#         while i <len(nums):
#             a = nums.count(nums[i])
#             if a > 1:
#                 for j in range(a-1):
#                     nums.remove(nums[i])
#             i += 1
#         return len(nums)

#THIRD
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

nums = [3,0,0,0]
test = Solution()
print(test.removeDuplicates(nums))
