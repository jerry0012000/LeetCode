# 怎么超时了啊
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         outputList = []
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if i != j:
#                     product = product * nums[j]
#             outputList.append(product)
#         return outputList
# 重写一个
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputList = []
        product = 1
        # 为了避免重复计算，先求出所有数之和，减少一层for循环
        for i in range(len(nums)): 
            product = product * nums[i]
        # 被去除的正好是0，计算一次for循环，算出其他数的和
        for j in range(len(nums)):
            if nums[j] == 0:
                tempProduct = 1
                for k in range(len(nums)):
                    if k != j:
                        tempProduct = tempProduct * nums[k]
                outputList.append(tempProduct)
            # 被去除的数不是0，直接所有数之和除一下就好了
            else:
                outputList.append(int(product/nums[j]))
        return outputList
        # 偷懒成功，大部分情况一次除法就可以搞定，无需每次计算多个乘法
