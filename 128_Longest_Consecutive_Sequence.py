class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sortedNums = nums
        sortedNums.sort() # 先筛
        print(sortedNums)
        newSortedNums = [] # 再去重
        # 注释掉的几行是优化前会导致复杂度增加的，in的话每次遍历整个列表，比较耗时
        # for i in range(len(sortedNums)):
        #     if sortedNums[i] not in newSortedNums:
        #         newSortedNums.append(sortedNums[i])
        newSortedNums.append(sortedNums[0])
        for i in range(1,len(sortedNums)):
            if sortedNums[i] != newSortedNums[-1]:
                newSortedNums.append(sortedNums[i]) # 因为已经筛了，是升序的，就直接比最后一位
        print(newSortedNums)
        maxLength = 1
        length = 1
        for i in range(1,len(newSortedNums)):
            if (newSortedNums[i] == newSortedNums[i-1] + 1):
                length += 1
                if length > maxLength:
                    maxLength = length
            else:
                length = 1
        return maxLength # 这题好像可以当成0-1背包问题？待探究
