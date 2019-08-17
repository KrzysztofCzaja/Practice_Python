# https://leetcode.com/problems/climbing-stairs/
# https://leetcode.com/problems/climbing-stairs/discuss/25583/Climb-the-stair-in-a-DP-and-Python-way-O(n)-42ms
#FIRST
# class Solution:
#     def climbStairs(self, n) -> int:
#         a, b = 1, 1
#         for i in range(n):
#             a, b = b, a + b
#         return a
#SECOND Dynamic Programing
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}
        ways[1],ways[2] = 1,2
        for i in range(3,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]




test = Solution()
print(test.climbStairs(6))