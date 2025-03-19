class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        else:
            # longestSubstr = ""
            length = 0
            for i in range(len(s)-1):
                subStr = s[i]
                # print(subStr)
                for j in range(i+1,len(s)):
                    if (s[j] in subStr):
                        break
                    else:
                        subStr += s[j]
                if len(subStr) > length:
                    # longestSubstr = subStr
                    length = len(subStr)
            return length
