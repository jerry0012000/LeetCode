class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        else:
            # remainNums = []
            # for i in range(len(nums)):
            #     remainNums.append(nums[i])
            remainNums = nums
            for i in range(len(nums)): # 用于比较的数
                for j in range(len(remainNums)): # 看看是否有第二个
                    if (nums[i] == remainNums[j] and i != j):
                        # 为了防止False和0混淆，只能出此下策了......
                        remainNums[j] = 'False'
                        remainNums[i] = 'False'
                        break
            # for l in range(len(remainNums)):
            #     print(remainNums[l])
            for k in remainNums:
                if k != 'False':
                    return k
