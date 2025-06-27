class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        
        # Create pairs of position and speed for each car
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])
        
        # 远的在前面，看看后面的车能不能追上前面的
        # Sort the pairs based on position in descending order
        pairs = sorted(pairs)[::-1]
        print(pairs)

        # Iterate through the sorted pairs
        for p, s in pairs:
            # 计算当前车辆到达终点所需时间
            # Calculate time to reach the target for the current car
            time = (target - p) / s

            # Add the time to the stack
            stack.append(time)

            # 如果后面的车追上前面的了，去掉前面的，看作一个整体。
            # Check if there are at least two cars in the stack and the current car
            # takes less or equal time than the previous car. If so, pop the previous car.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The length of the stack represents the number of car fleets
        return len(stack)
