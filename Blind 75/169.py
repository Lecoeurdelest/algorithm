class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = nums[0]
        for value in nums:
            if value == element:
                count += 1
            else:
                count -= 1

            if count == 0:
                element = value
                count += 1
        return element