class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_len = set(nums)
        return len(nums_len) < len(nums)