class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if (length==1):
            return cost[0]
        elif (length==2):
            return min(cost[0],cost[1])
        dp = [0] * (length+1)
        print(dp)
        dp[1] = cost[0]
        dp[2] = cost[1]
        for i in range(3,length+1):
            dp[i] = cost[i-1] + min(dp[i-1],dp[i-2])
        print(dp)
        return min(dp[length],dp[length-1])
