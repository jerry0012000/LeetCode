class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        print(nums)
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        print(dic.items())
        ansList = []
        for i in range(k):
            ans = max(dic, key=lambda x:dic[x])
            ansList.append(ans)
            del dic[ans]
        print(ansList)
        return ansList
