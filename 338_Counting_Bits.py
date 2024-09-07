class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2) # 表达式 i >> 1 是位运算中的右移运算符（>>），它将整数 i 的二进制表示向右移动一位。相当于将 i 除以 2 取整，舍弃余数。
        return counter
