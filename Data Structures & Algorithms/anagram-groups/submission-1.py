class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            anagrams = found.get(sortedStr, [])
            if len(anagrams) != 0:
                anagrams.append(str)
                found[sortedStr] = anagrams
            else:
                found[sortedStr] = [str]
        result = []
        for anagrams in found.values():
            result.append(anagrams)
        return result
        