class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            y = target - nums[x]
            if y in nums:
                if y != nums[x]:
                    return [x, nums.index(target - nums[x])]
                elif nums.count(y) > 1:
                    return [x, nums.index(y, x + 1)]
