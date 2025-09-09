class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highSpeed = max(piles)
        lowSpeed = 1
        while lowSpeed <= highSpeed:
            mid = (lowSpeed + highSpeed) // 2
            hours = sum([math.ceil(i / mid) for i in piles]) # ceil(a/b) = (a + b - 1) // b
            # //是向下取整, (i + mid - 1) // mid 代替 math.ceil(i / mid)
            if hours <= h:
                highSpeed = mid - 1 # 很快吃完减速
            else:
                lowSpeed = mid + 1 # 吃不完加速
        return lowSpeed
