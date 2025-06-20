class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if (target < nums[left] or target > nums[right]):
            return -1
        while (left <= right):
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            elif (target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
