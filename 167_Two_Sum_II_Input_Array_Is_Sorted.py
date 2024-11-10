class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 这个会超时
        # returnList = []
        # for j in range(len(numbers):
        #     for k in range(j+1,len(numbers)):
        #         if numbers[j] + numbers[k] == target:
        #             returnList.append(j+1)
        #             returnList.append(k+1)
        # return returnList
        sumList = []
        returnList = []
        numSet = set(numbers)
        innerloopBreak = False
        for j in numSet:
            for k in numSet:
                # print("j:", j)
                # print("k:", k)
                if j + k == target:
                    if j != k:
                        # print("j!=k")
                        sumList.append(j)
                        sumList.append(k)
                        print(sumList)
                        returnList.append(numbers.index(j)+1) # 修复起始为0的bug
                        returnList.append(numbers.index(k)+1)
                        innerloopBreak = True
                        break
                    else:
                        # print("j==k")
                        returnList.append(numbers.index(j)+1)
                        for m in range(len(numbers)-1,-1,-1):
                            if k == numbers[m]:
                                returnList.append(m+1)
                                innerloopBreak = True
                                break
            if innerloopBreak == True:
                break # 修复外循环防止重复
        returnList.sort() # 防止target是负数
        return returnList
