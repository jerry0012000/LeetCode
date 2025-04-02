class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # empty stack
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)): # looping through every temp in temperature
            while stack and temperatures[stack[-1]] < temperatures[i]: # while stack is not empty and the last element in the stack is less than current temp
                index = stack.pop() # we will pop that element from the stack and assign it to index
                result[index] = i - index # calculate result by subtracting current temp from index
            stack.append(i) # if stack is already, we append that temp to our stack
        return result
        # 超时
        # output = []
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         flag = 0
        #         if temperatures[j] > temperatures[i]:
        #             output.append(j - i)
        #             flag = 1
        #             break
        #     if flag == 0:
        #         output.append(0)
        # output.append(0)
        # return output
