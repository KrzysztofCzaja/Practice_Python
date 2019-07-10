#https://leetcode.com/problems/reverse-integer/
# #FIRST
# class Solution:
#     def reverse(self, x: int) -> int:
#         str_number = str(x)
#         if x<0:
#             reversed_str_number = str_number[:0:-1]
#         else:
#             reversed_str_number = str_number[::-1]
#         reversed_number = int(reversed_str_number)
#         if x<0:
#             reversed_number *= -1
#         if reversed_number>2147483647 or reversed_number<-2147483648:
#             return 0
#         else:
#             return reversed_number
#
#SECOND to not overflow
class Solution:
    def reverse(self, x: int) -> int:
        str_number = str(x)
        high_upperbound = "2147483647"
        low_uppebound = "2147483648"
        i = 0
        if x<0:
            reversed_str_number = str_number[:0:-1]
            if len(reversed_str_number)== len(low_uppebound):
                while len(reversed_str_number)>i:
                    first = int(reversed_str_number[i])
                    second = int(low_uppebound[i])
                    if first == second:
                        i+=1
                    elif first < second:
                        i = len(reversed_str_number)
                    else:
                        return 0
            elif len(reversed_str_number) > len(low_uppebound):
                return 0

        else:
            reversed_str_number = str_number[::-1]
            if len(reversed_str_number) == len(high_upperbound):
                while len(reversed_str_number)>i:
                    first = int(reversed_str_number[i])
                    second = int(high_upperbound[i])
                    if first == second:
                        i += 1
                    elif first < second:
                        i = len(reversed_str_number)
                    else:
                        return 0
            elif len(reversed_str_number) > len(low_uppebound):
                return 0
        reversed_number = int(reversed_str_number)
        if x < 0:
            reversed_number *= -1
        return reversed_number


test = Solution()
x = test.reverse(-2147483412)
print(x)