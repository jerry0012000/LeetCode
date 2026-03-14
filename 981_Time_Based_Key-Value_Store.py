class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap.get(key).append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap: # self.hashmap是一个字典, self.hashmap[key]是一个 list, 而这个list里面存的是[[timestamp, value], [timestamp, value], ...]
            return ""   
 
        key_values = self.hashmap[key]
        result = ""
        left, right = 0, len(key_values) - 1

        while left <= right:
            mid = (right + left) // 2
            key_timestamp, key_value = key_values[mid][0], key_values[mid][1]
            if key_timestamp <= timestamp:
                left = mid + 1
                result = key_value
            else:
                right = mid - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
