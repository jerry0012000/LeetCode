# 枚举法会超时
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         dp = [[0 for _ in range(len(height))] for _ in range((len(height)))]
#         for i in range(len(height)-1):
#             for j in range(i+1,len(height)):
#                 dp[i][j] = min(height[i],height[j])*(j-i)
#         # print(dp)
#         mostWater = 0
#         for k in range(len(height)):
#             if max(dp[k]) > mostWater:
#                 mostWater = max(dp[k])
#         return mostWater
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 看答案，这题居然要用指针？？？
        left = 0
        right = len(height) - 1
        mostWater = 0
        while left < right:
            currentWater = min(height[left],height[right])*(right-left)
            mostWater = max(mostWater,currentWater)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mostWater
