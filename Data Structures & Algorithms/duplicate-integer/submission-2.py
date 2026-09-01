class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for x in nums:
            myset.add(x)
        if len(nums) != len(myset):
            return True
        else:
            return False
        