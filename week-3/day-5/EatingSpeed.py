class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) >> 1
            total_hours = 0
            for p in piles:
                total_hours += (p/mid)
            if total_hours <= h:
                result = min(result, mid)
                right = mid -1
            else:
                left = mid + 1
        return result