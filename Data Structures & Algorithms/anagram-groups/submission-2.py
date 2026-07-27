class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            anagrams = found.get(sortedStr, [])
            anagrams.append(str)
            found[sortedStr] = anagrams
        result = []
        for anagrams in found.values():
            result.append(anagrams)
        return result
        