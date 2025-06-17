class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        #  This is a helper function that uses depth-first search (DFS) to explore all possible combinations.
        def dfs(openP, closeP, s):
            # Base case: If the number of open and close parentheses are equal and the total length of the string is 2 * n, it means we have a valid combination.
            if openP == n and closeP == n: #左括号和右括号数量都等于n，当前结果添加到序列就可以了
                res.append(s)
                return
            # If the number of open parentheses used (openP) is less than n, we can add another open parenthesis.
            # 左括号存在，那么一定可以添加到括号序列中
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            # If the number of close parentheses used (closeP) is less than the number of open parentheses, we can add a close parenthesis to maintain balance.
            # 右括号小于n且右括号数量小于左括号数量
            if closeP < n and closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res
