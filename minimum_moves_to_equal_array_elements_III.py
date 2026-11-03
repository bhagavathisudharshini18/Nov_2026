class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        moves = 0
        for num in nums:
            moves += max_num - num
        return moves
