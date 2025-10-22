class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 1
        for index, value in enumerate(nums):
            if(nums[index] - 1 not in nums_set):
                length = 1
                while(value + 1 in nums_set):
                    length += 1
                    value += 1
                    nums_set.remove(value)
                max_length = max(length, max_length)
        return 0 if len(nums) == 0 else max_length