class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0]) # 矩阵的长和宽
        low, high = 0, m * n - 1 # 最小的和最大的数的索引
        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            if mid_value == target:
                return True
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
