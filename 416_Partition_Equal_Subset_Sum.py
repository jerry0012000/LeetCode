class Solution:
    # from itertools import combinations # 这玩意可以用，就是会爆内存、爆PyCharm、爆任务管理器......
    def canPartition(self, nums: List[int]) -> bool:
        # 可以认为是0-1背包，放进背包的和没放进背包的物品重量相等。
        if sum(nums) % 2 != 0:
            return False
        else:
            size = len(nums)
            target = int(sum(nums)/2) # 放进背包的物品的重量
            # sorted_nums = sorted(nums)
            dp = [[False for _ in range(target + 1)] for _ in range(size)]
            for i in range(target + 1): # 先写第一行，看看第一个数是不是正好就是背包一半的，装进背包就结束。
                dp[0][i] = False if nums[0] != i else True
            for i in range(1,size): # 外循环：有多少个元素
                for j in range(target + 1): # 内循环：背包能不能装出这个重量
                    if j >= nums[i]: # 如果背包还没装满
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]] 
                        # 左：不选择nums[i], [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，这些数的和能不能等于j跟上一个区间没区别。
                        # 右：选择nums[i], 在[0, i - 1]这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]
                    else:
                        dp[i][j] = dp[i - 1][j] # 超重了
            return dp[-1][-1]
            # print(sorted_nums)
            # for i in range(len(sorted_nums)):
            #     if sorted_nums[i] == target:
            #         return True
            # for i in range(len(nums)):
            #     for c in list(itertools.combinations(nums,i+1)):
            #         s = sum(c)
            #         if s == target:
            #             return True
            return False
