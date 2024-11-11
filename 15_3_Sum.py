# 老代码（超时）
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             j = i+1
#             k = j+1
#             while (j<len(nums)-1):
#                 if (nums[i] + nums[j] + nums[k]) == 0:
#                     tempList = []
#                     tempList.append(nums[i])
#                     tempList.append(nums[j])
#                     tempList.append(nums[k])
#                     # tempList.sort()不要在循环里面排序！三个三个一排比在外面排好要复杂多了
#                     if tempList not in results:
#                         results.append(tempList)
#                 if (k<len(nums)-1): # k not reach the end一定要-1，这个地方是个大坑！
#                     k += 1
#                 else: # k reach the end
#                     j += 1
#                     k = j+1
#         return results
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 避免出现nums[0] = nums[-1]的情况，典型案例：[0,0,0]
                continue
            j = i+1
            k = len(nums)-1
            while (j<k):
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else: # total == 0
                    tempList = []
                    tempList.append(nums[i])
                    tempList.append(nums[j])
                    tempList.append(nums[k])
                    # tempList.sort()不要在循环里面排序！三个三个一排比在外面排好要复杂多了
                    results.append(tempList)
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return results
