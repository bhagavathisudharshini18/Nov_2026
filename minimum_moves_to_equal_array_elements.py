class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        return sum(nums) - len(nums) * minimum
