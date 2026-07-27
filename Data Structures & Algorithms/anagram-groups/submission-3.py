class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c) - ord('a')] += 1
            found[tuple(freq)].append(str)
        result = []
        for anagrams in found.values():
            result.append(anagrams)
        return result
        