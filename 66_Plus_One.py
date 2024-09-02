class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempList = []
        output = []
        add = 0
        for i in range(len(digits)-1,-1,-1):
            # print(digits[i])
            # print(i)
            # print(len(digits)-1)
            if i == len(digits)-1: # 个位
                if (digits[i] != 9): # 不进位
                    tempList.append(digits[i] + 1)
                else: # 进位
                    tempList.append(0)
                    add = 1
            else: # 不是个位
                if add == 1:
                    if (digits[i] != 9): # 不进位
                        tempList.append(digits[i] + 1)
                        add = 0 # 不进位也别忘了重置！
                    else: # 进位
                        tempList.append(0)
                        add = 1
                else:
                    tempList.append(digits[i])
                    add = 0 # 重置进位
        if digits[0] == 9 and add == 1: # 加1后整个List多了一位
            tempList.append(1) # 是否多加一位？
        # print(tempList)
        # print(type(tempList))
        for j in range(len(tempList)-1,-1,-1):
            output.append(tempList[j]) # 翻转，实测reverse()不能用
        return output
