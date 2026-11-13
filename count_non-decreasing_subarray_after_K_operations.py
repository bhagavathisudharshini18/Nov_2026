class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            count = 1

            while dq and dq[0][0] < x:
                val, cnt = dq.popleft()
                cost += (x - val) * cnt
                count += cnt

            if dq and dq[0][0] == x:
                val, cnt = dq.popleft()
                count += cnt

            dq.appendleft((x, count))

            while cost > k:
                val, cnt = dq[-1]
                cost -= val - nums[right]

                if cnt == 1:
                    dq.pop()
                else:
                    dq[-1] = (val, cnt - 1)

                right -= 1

            ans += right - left + 1

        return ans
