from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ordered_nums = defaultdict(int)
        for num in nums:
            ordered_nums[num] += 1
        count = 0
        while count <= len(nums):
            if count not in ordered_nums.keys():
                return count
            else:
                count += 1

