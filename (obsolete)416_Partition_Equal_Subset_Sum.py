class Solution:
    import itertools
    # from itertools import combinations
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums)/2
            # sorted_nums = sorted(nums,reverse=True)
            # print(sorted_nums)
            # for i in range(len(sorted_nums)):
            #     if sorted_nums[i] == target:
            #         return True
            for i in range(len(nums)):
                for c in list(itertools.combinations(nums,i+1)):
                    s = sum(c)
                    if s == target:
                        return True
            return False
