class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for a in arr1:
            valid = True
            for b in arr2:
                if abs(a - b) <= d:
                    valid = False
                    break
            if valid:
                count += 1
        return count
