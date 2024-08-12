class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        sorted_potions = sorted(potions)
        result = []
        for i in spells:
            count = len(sorted_potions) - (sorted_potions, (success + i - 1) // i)
            result.append(count)
        return result   