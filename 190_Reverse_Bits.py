class Solution:
    def reverseBits(self, n: int) -> int:
        list = []
        strN = str(bin(n))[2:]
        # print(strN)
        for i in range(len(strN)-1,-1,-1):
            list.append(strN[i])
        if len(list) < 32:
            for j in range(len(strN),32):
                list.append('0')
        # print(list)
        strReverseN = "0b" + ''.join(list)
        # print(strReverseN)
        return int(strReverseN,2) # 逗号表示由二进制转来
