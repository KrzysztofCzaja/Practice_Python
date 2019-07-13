# # https://leetcode.com/problems/longest-common-prefix/
#FIRST
# class Solution:
#     def longestCommonPrefix(self, strs):
#         empty=""
#         if len(strs) != 0:
#             letter = 0
#             min_lenght = len(min(strs,key=len))
#             if min_lenght>0:
#                 prefix = []
#                 while letter<min_lenght:
#                     temp = []
#                     for word in range(len(strs)):
#                         temp.append(strs[word][letter])
#                     if all(elem == temp[0] for elem in temp):
#                         prefix.append(temp[0])
#                     else:
#                         if len(prefix) == 0:
#                             return ""
#                         else:
#                             return ''.join(prefix)
#                     letter += 1
#                 return ''.join(prefix)
#             return ""
#

# SECOND FIXED SOLUTION
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) != 0:
            letter = 0
            min_lenght = len(min(strs,key=len))
            while letter<min_lenght:
                temp = []
                for word in range(len(strs)):
                    temp.append(strs[word][letter])
                if all(elem == temp[0] for elem in temp):
                    prefix += temp[0]
                else:
                    break
                letter += 1
        return prefix
# #THIRD
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pre = ''
#         for args in zip(*strs):
#             if all(arg == args[0] for arg in args):
#                 pre += args[0]
#             else:
#                 break
#         return pre
#
#




word = ["flower","flow","flight"]
test = Solution()
print(test.longestCommonPrefix(word))