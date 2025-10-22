class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            if(map.get(value) is not None):
                return [map.get(value), index]
            map[target - value] = index
        return []