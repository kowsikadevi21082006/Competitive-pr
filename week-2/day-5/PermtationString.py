class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        need, have, left = (s1), (), 0
        for right, ch in enumerate(s2):
            if ch not in need:
                have.clear()
                left = right + 1
                continue
            have[ch] += 1
            while have[ch] > need[ch]:
                have[s2[left]] -= 1
                left += 1
                
            if right - left + 1 == len(s1): return True

        return False