class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # 基本上跟dict一样，但可以避免无效key
        for word in strs: # 遍历每个字符串
            sorted_word = ''.join(sorted(word)) # 创建字典字段
            anagram_map[sorted_word].append(word) # 往字段里加组合
        return list(anagram_map.values())
