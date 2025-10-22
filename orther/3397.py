class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        uniq_nums = set()
        pos = -10**18
        for num in nums:
            target = max(pos, num -k)
            if target <= num + k:
                uniq_nums.add(target)
                pos = target + 1

        return len(uniq_nums)