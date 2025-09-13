class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # 左半边有序
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半边有序
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
        # if target not in nums:
        #     return -1
        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 2:
        #     if target != nums[0]:
        #         return 1
        #     else:
        #         return 0
        # for i in range(1,len(nums)):
        #     if nums[i] < nums[i-1]:
        #         m = i
        #         break
        # l = 0
        # r = len(nums)
        # # print(l,m,r)
        # if (target > nums[m-1]) or (target < nums[m]):
        #     return -1
        # if target > l:
        #     r = m-1
        #     while l <= r:
        #         mid = int((l+r)/2)
        #         if target == nums[mid]:
        #             return mid
        #         elif (target > nums[mid]):
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return -1
        # if target < r:
        #     l = m
        #     # print(l)
        #     # print(r)
        #     while l <= r:
        #         mid = int((l+r)/2)
        #         if target == nums[mid]:
        #             return mid
        #         elif (target > nums[mid]):
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return -1
