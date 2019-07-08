#https://leetcode.com/problems/two-sum/
#FIRST
# class Solution(object):
#     def twoSum(self,nums,target):
#         """
#                 :type nums: List[int]
#                 :type target: int
#                 :rtype: List[int]
#                 """
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]

#SECOND BEST
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dict = {}
#         for i in range(len(nums)):
#             if target-nums[i] not in dict:
#                 dict[nums[i]]=i
#             else:
#                 return [dict[target-nums[i]],i]
#SECOND //ANOTHER SIMILAR WAY
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target-nums[i]]=i


nums = [2,7,11,15]
target = 9
test = Solution()
print(test.twoSum(nums,target))
