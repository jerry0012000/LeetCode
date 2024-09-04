class Solution:
    def hammingWeight(self, n: int) -> int:
        p = 0 # 最大的一位是2的几次方？
        for i in range(1,32):
            if pow(2,i-1) <= n and pow(2,i) > n:
                p = i-1
                break
        binary_str = ""
        for j in range(p,-1,-1):
            if n >= pow(2,j):
                n -= pow(2,j)
                binary_str += str(1)
            else:
                binary_str += str(0)
        print(binary_str)
        # 至此，10进制转换为2进制
        return binary_str.count('1') # 数一下1的数量
