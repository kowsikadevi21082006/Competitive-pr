class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = dict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())