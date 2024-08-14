class Trie:
    def __init__(self):
        self.root = {}

    def count_add(self, word):
        current_dict = self.root
        ans=0
        for a,b in zip(word,word[::-1]):
            current_dict = current_dict.setdefault((a,b), {'_end_':0})
            ans+=current_dict['_end_']
        current_dict['_end_'] += 1
        return ans

class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        tr = Trie()
        return sum(tr.count_add(word) for word in words)
        