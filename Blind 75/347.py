class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for value in nums:
            map[value] = map.get(value, 0) + 1
        for key, value in map.items():
            if len(result) < k:
                result.append(key)
            else:
                min_key = min(result, key=lambda x: map[x])
                if value > map[min_key]:
                    result.remove(min_key)
                    result.append(key)
        return result